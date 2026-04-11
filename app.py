#!/usr/bin/env python3
"""
Swimnerd AI API - Static Build Version
Uses pre-built wiki_content.json (no GitHub API calls)
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from pathlib import Path

app = Flask(__name__)
CORS(app)

# Configuration
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
MODEL = "claude-3-5-haiku-20241022"

# Load wiki content from static JSON file
WIKI_DATA = None

def load_wiki_content():
    """Load pre-built wiki content from JSON file"""
    global WIKI_DATA
    
    if WIKI_DATA:
        return WIKI_DATA
    
    wiki_file = Path(__file__).parent / 'wiki_content.json'
    
    try:
        print(f"Loading wiki content from {wiki_file}")
        with open(wiki_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            WIKI_DATA = data['articles']
            print(f"✓ Loaded {len(WIKI_DATA)} articles")
            return WIKI_DATA
    except Exception as e:
        print(f"Error loading wiki content: {e}")
        return []

def search_wiki(query, max_results=5):
    """
    Keyword search across wiki articles
    """
    articles = load_wiki_content()
    
    if not articles:
        return []
    
    results = []
    query_lower = query.lower()
    query_words = query_lower.split()
    
    for article in articles:
        content = article['content']
        content_lower = content.lower()
        filename_lower = article['filename'].lower()
        path_lower = article['path'].lower()
        
        # Score based on keyword matches
        score = 0
        for word in query_words:
            if len(word) > 2:
                score += content_lower.count(word)
        
        # Boost if filename matches
        for word in query_words:
            if len(word) > 2:
                if word in filename_lower:
                    score += 10
                if word in path_lower:
                    score += 5
        
        # Special boost for exact topic matches
        if 'cam mcevoy' in query_lower and 'cam mcevoy' in content_lower:
            score += 100
        if 'dave salo' in query_lower and 'dave salo' in content_lower:
            score += 100
        if 'bob bowman' in query_lower and 'bob bowman' in content_lower:
            score += 100
        
        if score > 0:
            results.append({
                'file': article['filename'],
                'path': article['path'],
                'content': content,
                'score': score
            })
    
    # Sort by score and return top results
    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:max_results]

@app.route('/api/ask', methods=['POST'])
def ask():
    """
    Main API endpoint for asking questions
    """
    data = request.json
    question = data.get('question', '')
    
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    # Search wiki
    search_results = search_wiki(question, max_results=3)
    
    if not search_results:
        return jsonify({
            'answer': "I don't have enough information in my knowledge base to answer that question. The Swimnerd Wiki is still being built out. Try asking about Bob Bowman, Dave Salo, Cam McEvoy, or general swimming training methodology.",
            'sources': []
        })
    
    # Build context from top results
    context_parts = []
    for r in search_results:
        context_parts.append(f"**{r['path']}**\n\n{r['content'][:3000]}")  # 3000 chars per article
    
    context = "\n\n---\n\n".join(context_parts)
    
    # Call Anthropic API
    if not ANTHROPIC_API_KEY:
        return jsonify({
            'answer': f"Based on the wiki content:\n\n{context[:1000]}",
            'sources': [r['path'] for r in search_results],
            'note': 'API key not configured - showing raw context'
        })
    
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        
        prompt = f"""You are a swimming coaching expert. Answer the question based ONLY on the provided wiki content. Be specific and cite details from the content.

WIKI CONTENT:
{context}

QUESTION: {question}

ANSWER (be concise, specific, and cite details from the wiki):"""
        
        message = client.messages.create(
            model=MODEL,
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        answer = message.content[0].text
        
        return jsonify({
            'answer': answer,
            'sources': [r['path'] for r in search_results]
        })
        
    except Exception as e:
        print(f"Anthropic API error: {e}")
        return jsonify({
            'answer': f"I found relevant information but couldn't generate a full response. Here's what I found:\n\n{context[:500]}",
            'sources': [r['path'] for r in search_results],
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    articles = load_wiki_content()
    
    return jsonify({
        'status': 'ok',
        'wiki_articles': len(articles),
        'anthropic_configured': bool(ANTHROPIC_API_KEY),
        'model': MODEL,
        'mode': 'static'
    })

@app.route('/api/stats', methods=['GET'])
def stats():
    """Show wiki content stats"""
    articles = load_wiki_content()
    
    # Count by category
    categories = {}
    for article in articles:
        path_parts = article['path'].split('/')
        if len(path_parts) > 1:
            category = path_parts[0]
        else:
            category = 'root'
        
        categories[category] = categories.get(category, 0) + 1
    
    return jsonify({
        'total_articles': len(articles),
        'categories': categories
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting Swimnerd AI API (Static Build) on port {port}")
    print(f"Anthropic API key configured: {bool(ANTHROPIC_API_KEY)}")
    load_wiki_content()  # Load on startup
    app.run(host='0.0.0.0', port=port)
