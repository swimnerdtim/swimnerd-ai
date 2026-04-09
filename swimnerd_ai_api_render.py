#!/usr/bin/env python3
"""
Swimnerd AI API - Render Deployment Version
Fetches wiki content from GitHub (no local files needed)
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
import requests
from pathlib import Path

app = Flask(__name__)
CORS(app)

# Configuration
GITHUB_WIKI_URL = "https://api.github.com/repos/swimnerdtim/swimnerd-wiki/contents/wiki"
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
MODEL = "claude-haiku-4-20250514"

# Cache for wiki content (refresh every hour)
wiki_cache = {}
cache_timestamp = 0

def fetch_wiki_from_github():
    """Fetch all wiki markdown files from GitHub"""
    global wiki_cache, cache_timestamp
    import time
    
    # Use cache if less than 1 hour old
    if wiki_cache and (time.time() - cache_timestamp) < 3600:
        return wiki_cache
    
    print("Fetching wiki content from GitHub...")
    articles = []
    
    try:
        # Get all .md files from wiki directory
        response = requests.get(GITHUB_WIKI_URL, timeout=10)
        response.raise_for_status()
        
        files = response.json()
        
        for file in files:
            if file['type'] == 'file' and file['name'].endswith('.md'):
                # Fetch file content
                content_response = requests.get(file['download_url'], timeout=10)
                if content_response.status_code == 200:
                    articles.append({
                        'filename': file['name'],
                        'content': content_response.text,
                        'path': file['path']
                    })
            elif file['type'] == 'dir':
                # Recursively fetch from subdirectories
                subdir_response = requests.get(file['url'], timeout=10)
                if subdir_response.status_code == 200:
                    subfiles = subdir_response.json()
                    for subfile in subfiles:
                        if subfile['name'].endswith('.md'):
                            content_response = requests.get(subfile['download_url'], timeout=10)
                            if content_response.status_code == 200:
                                articles.append({
                                    'filename': subfile['name'],
                                    'content': content_response.text,
                                    'path': subfile['path']
                                })
        
        wiki_cache = articles
        cache_timestamp = time.time()
        print(f"Fetched {len(articles)} articles from GitHub")
        return articles
        
    except Exception as e:
        print(f"Error fetching from GitHub: {e}")
        return wiki_cache if wiki_cache else []

def search_wiki(query, max_results=5):
    """
    Keyword search across wiki articles
    """
    articles = fetch_wiki_from_github()
    
    if not articles:
        return []
    
    results = []
    query_lower = query.lower()
    query_words = query_lower.split()
    
    for article in articles:
        content = article['content']
        content_lower = content.lower()
        filename_lower = article['filename'].lower()
        
        # Score based on keyword matches
        score = 0
        for word in query_words:
            if len(word) > 2:
                score += content_lower.count(word)
        
        # Boost if filename matches
        for word in query_words:
            if len(word) > 2 and word in filename_lower:
                score += 10
        
        # Special boost for exact topic matches
        if 'cam mcevoy' in query_lower and 'cam mcevoy' in content_lower:
            score += 50
        if 'dave salo' in query_lower and 'dave salo' in content_lower:
            score += 50
        
        if score > 0:
            results.append({
                'file': article['filename'],
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
    context = "\n\n---\n\n".join([
        f"**{r['file']}**\n\n{r['content'][:2000]}"  # Limit to 2000 chars per article
        for r in search_results
    ])
    
    # Call Anthropic API
    if not ANTHROPIC_API_KEY:
        return jsonify({
            'answer': f"Based on the wiki content:\n\n{context[:1000]}",
            'sources': [r['file'] for r in search_results],
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
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        
        answer = message.content[0].text
        
        return jsonify({
            'answer': answer,
            'sources': [r['file'] for r in search_results]
        })
        
    except Exception as e:
        print(f"Anthropic API error: {e}")
        return jsonify({
            'answer': f"I found relevant information but couldn't generate a full response. Here's what I found:\n\n{context[:500]}",
            'sources': [r['file'] for r in search_results],
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    articles = fetch_wiki_from_github()
    
    return jsonify({
        'status': 'ok',
        'wiki_articles': len(articles),
        'anthropic_configured': bool(ANTHROPIC_API_KEY),
        'model': MODEL
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting Swimnerd AI API on port {port}")
    print(f"Anthropic API key configured: {bool(ANTHROPIC_API_KEY)}")
    app.run(host='0.0.0.0', port=port)
