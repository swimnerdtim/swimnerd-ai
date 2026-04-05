#!/usr/bin/env python3
"""
Swimnerd AI API - Proof of Concept
Simple API that searches wiki and calls LLM for answers
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from pathlib import Path
import anthropic

app = Flask(__name__)
CORS(app)  # Enable CORS for local testing

# Configuration
WIKI_PATH = Path(__file__).parent / "wiki"
CLAUDE_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")  # Set in environment

def search_wiki(query, max_results=3):
    """
    Simple keyword search across wiki markdown files.
    Returns list of relevant file contents.
    """
    results = []
    query_lower = query.lower()
    
    # Search all .md files in wiki
    for md_file in WIKI_PATH.rglob("*.md"):
        with open(md_file, 'r') as f:
            content = f.read()
            # Simple relevance: check if query keywords appear in content
            if any(word in content.lower() for word in query_lower.split()):
                results.append({
                    'file': str(md_file.relative_to(WIKI_PATH)),
                    'content': content[:2000]  # First 2000 chars for POC
                })
    
    return results[:max_results]

def search_books_json(query):
    """
    Search the Bob Bowman transcripts JSON for relevant content
    """
    transcripts_file = Path(__file__).parent / "bob_bowman_data" / "Transcripts"
    results = []
    
    # For POC, just return a sample if the directory exists
    if transcripts_file.exists():
        txt_files = list(transcripts_file.glob("*.txt"))
        if txt_files:
            # Read first transcript as example
            with open(txt_files[0], 'r') as f:
                content = f.read()[:1500]
                results.append({
                    'source': 'Bob Bowman Transcripts',
                    'content': content
                })
    
    return results

@app.route('/api/ask', methods=['POST'])
def ask():
    """
    Main API endpoint for asking questions
    """
    data = request.json
    question = data.get('question', '')
    
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    # Search wiki for relevant content
    wiki_results = search_wiki(question)
    book_results = search_books_json(question)
    
    # Build context from results
    context_parts = []
    
    if wiki_results:
        context_parts.append("=== Wiki Knowledge ===")
        for result in wiki_results:
            context_parts.append(f"\n## {result['file']}\n{result['content']}")
    
    if book_results:
        context_parts.append("\n\n=== Coach Transcripts ===")
        for result in book_results:
            context_parts.append(f"\n{result['content']}")
    
    context = "\n".join(context_parts)
    
    # For POC: If no CLAUDE_API_KEY, return mock response
    if not CLAUDE_API_KEY:
        return jsonify({
            'answer': f"[POC Mode - No API key set]\n\nYou asked: {question}\n\nFound {len(wiki_results)} wiki results and {len(book_results)} book results.\n\nIn production, this would call Claude API with the context to generate a personalized answer based on championship swimming knowledge.",
            'sources': len(wiki_results) + len(book_results),
            'mode': 'mock'
        })
    
    # Call Claude API
    try:
        client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
        
        message = client.messages.create(
            model="claude-sonnet-4",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": f"""You are a championship swimming coach with access to knowledge from Bob Bowman, elite training methodology books, and race analysis data.

Knowledge Base:
{context}

User Question: {question}

Provide a helpful, specific answer based on the knowledge above. If the knowledge base doesn't contain relevant information, say so and provide general swimming coaching advice."""
            }]
        )
        
        answer = message.content[0].text
        
        return jsonify({
            'answer': answer,
            'sources': len(wiki_results) + len(book_results),
            'mode': 'claude'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'answer': f"Error calling AI: {str(e)}\n\nSearched {len(wiki_results)} wiki pages.",
            'sources': len(wiki_results) + len(book_results),
            'mode': 'error'
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'wiki_path': str(WIKI_PATH),
        'wiki_exists': WIKI_PATH.exists(),
        'has_api_key': bool(CLAUDE_API_KEY)
    })

if __name__ == '__main__':
    print(f"Starting Swimnerd AI API...")
    print(f"Wiki path: {WIKI_PATH}")
    print(f"API key configured: {bool(CLAUDE_API_KEY)}")
    app.run(debug=True, port=5001, host='0.0.0.0')
