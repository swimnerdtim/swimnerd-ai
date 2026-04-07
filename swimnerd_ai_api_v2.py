#!/usr/bin/env python3
"""
Swimnerd AI API - Fixed Version
Simple API that searches wiki and calls LLM for answers
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from pathlib import Path

app = Flask(__name__)
CORS(app)  # Enable CORS for local testing

# Configuration
WIKI_PATH = Path(__file__).parent / "wiki"
CLAUDE_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")  # Set in environment

def search_wiki(query, max_results=5):
    """
    Improved keyword search with better scoring and more content.
    Returns list of relevant file contents.
    """
    results = []
    query_lower = query.lower()
    keywords = query_lower.split()
    
    # Search all .md files in wiki
    for md_file in WIKI_PATH.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                content_lower = content.lower()
                
                # Calculate relevance score
                score = 0
                for word in keywords:
                    score += content_lower.count(word)
                
                # Bonus for files matching topic (e.g., bob-bowman files for bowman questions)
                file_path_lower = str(md_file).lower()
                for word in keywords:
                    if word in file_path_lower:
                        score += 10  # Boost files with matching names
                
                if score > 0:
                    results.append({
                        'file': str(md_file.relative_to(WIKI_PATH)),
                        'content': content[:5000],  # Increased to 5000 chars
                        'score': score
                    })
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue
    
    # Sort by score (best matches first)
    results.sort(key=lambda x: x['score'], reverse=True)
    
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
            try:
                # Read first transcript as example
                with open(txt_files[0], 'r', encoding='utf-8') as f:
                    content = f.read()[:1500]
                    results.append({
                        'source': 'Bob Bowman Transcripts',
                        'content': content
                    })
            except Exception as e:
                print(f"Error reading transcripts: {e}")
    
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
    
    # Call Claude API with proper error handling
    try:
        # Import here to avoid issues if not installed
        import anthropic
        
        # Create client with minimal parameters
        client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
        
        # Create message
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": f"""You are a swimming coach. Answer the question using the knowledge provided.

Knowledge Base:
{context}

User Question: {question}

Provide a helpful, specific answer. Be direct and conversational. Don't say what you're trained on or explain your capabilities."""
            }]
        )
        
        answer = message.content[0].text
        
        return jsonify({
            'answer': answer,
            'sources': len(wiki_results) + len(book_results),
            'mode': 'claude'
        })
        
    except ImportError:
        return jsonify({
            'error': 'anthropic library not installed',
            'answer': f"Server configuration error: anthropic library missing.\n\nSearched {len(wiki_results)} wiki pages.",
            'sources': len(wiki_results) + len(book_results),
            'mode': 'error'
        }), 500
    except AttributeError as e:
        return jsonify({
            'error': f'Library version mismatch: {str(e)}',
            'answer': f"Server configuration error: {str(e)}\n\nThis usually means the anthropic library needs to be updated to version 0.40.0 or higher.",
            'sources': len(wiki_results) + len(book_results),
            'mode': 'error'
        }), 500
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
    try:
        import anthropic
        anthropic_version = anthropic.__version__
    except:
        anthropic_version = "not installed"
    
    return jsonify({
        'status': 'ok',
        'wiki_path': str(WIKI_PATH),
        'wiki_exists': WIKI_PATH.exists(),
        'has_api_key': bool(CLAUDE_API_KEY),
        'anthropic_version': anthropic_version
    })

if __name__ == '__main__':
    print(f"Starting Swimnerd AI API v2...")
    print(f"Wiki path: {WIKI_PATH}")
    print(f"Wiki exists: {WIKI_PATH.exists()}")
    print(f"API key configured: {bool(CLAUDE_API_KEY)}")
    
    try:
        import anthropic
        print(f"Anthropic library: {anthropic.__version__}")
    except:
        print("Anthropic library: NOT INSTALLED")
    
    app.run(debug=True, port=5001, host='0.0.0.0')
