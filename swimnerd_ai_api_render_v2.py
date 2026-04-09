#!/usr/bin/env python3
"""
Swimnerd AI API - Render Deployment Version v2
Fetches wiki content from GitHub's pre-built wikiData.json
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
import time

app = Flask(__name__)
CORS(app)

# Configuration
WIKI_DATA_URL = "https://raw.githubusercontent.com/swimnerdtim/swimnerd-wiki/main/src/wikiData.json"
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
MODEL = "claude-haiku-4-20250514"

# Cache for wiki content (refresh every hour)
wiki_cache = []
cache_timestamp = 0

def fetch_wiki_from_github():
    """Fetch pre-built wiki data from GitHub"""
    global wiki_cache, cache_timestamp
    
    # Use cache if less than 1 hour old
    if wiki_cache and (time.time() - cache_timestamp) < 3600:
        return wiki_cache
    
    print("Fetching wiki content from GitHub...")
    
    try:
        # Add cache-busting headers to bypass GitHub CDN cache
        headers = {
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache'
        }
        response = requests.get(WIKI_DATA_URL, headers=headers, timeout=10)
        response.raise_for_status()
        
        articles = response.json()
        
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
        title = article.get('title', '')
        description = article.get('description', '')
        content = article.get('content', '')
        category = article.get('category', '')
        
        title_lower = title.lower()
        desc_lower = description.lower()
        content_lower = content.lower()
        category_lower = category.lower()
        
        # Score based on keyword matches
        score = 0
        
        # Title matches (highest weight)
        for word in query_words:
            if len(word) > 2:
                if word in title_lower:
                    score += 50
                if word in desc_lower:
                    score += 20
                if word in category_lower:
                    score += 10
                score += content_lower.count(word)
        
        # Special boost for exact coach/athlete matches
        if 'cam mcevoy' in query_lower:
            if 'cam mcevoy' in title_lower or 'cam mcevoy' in content_lower:
                score += 100
        if 'dave salo' in query_lower:
            if 'dave salo' in title_lower or 'dave salo' in content_lower:
                score += 100
        if 'bob bowman' in query_lower:
            if 'bob bowman' in title_lower or 'bob bowman' in content_lower:
                score += 100
        
        if score > 0:
            results.append({
                'title': title,
                'content': content,
                'score': score,
                'category': category
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
        f"**{r['title']}** ({r['category']})\n\n{r['content'][:3000]}"  # Limit to 3000 chars per article
        for r in search_results
    ])
    
    # Call Anthropic API
    if not ANTHROPIC_API_KEY:
        return jsonify({
            'answer': f"Based on the wiki content:\n\n{context[:1000]}",
            'sources': [r['title'] for r in search_results],
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
            'sources': [r['title'] for r in search_results]
        })
        
    except Exception as e:
        print(f"Anthropic API error: {e}")
        return jsonify({
            'answer': f"I found relevant information but couldn't generate a full response. Here's what I found:\n\n{context[:500]}",
            'sources': [r['title'] for r in search_results],
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
        'model': MODEL,
        'data_source': 'GitHub wikiData.json'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting Swimnerd AI API v2 on port {port}")
    print(f"Anthropic API key configured: {bool(ANTHROPIC_API_KEY)}")
    print(f"Data source: {WIKI_DATA_URL}")
    app.run(host='0.0.0.0', port=port)
