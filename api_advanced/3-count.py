#!/usr/bin/python3
"""
Module that contains function to count words in Reddit API hot posts.

This module provides functionality to recursively query Reddit's API
and count occurrences of specified keywords in hot article titles.
"""

import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursive function that queries Reddit API and counts keywords
    in hot article titles
    
    Args:
        subreddit: the subreddit to query
        word_list: list of keywords to count
        word_count: dictionary to store word counts (for recursion)
        after: pagination parameter for Reddit API
    """
    if word_count is None:
        word_count = {}
        # Initialize word_count with lowercase keywords
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(word_lower, 0)
    
    # Set up headers to avoid Too Many Requests error
    headers = {'User-Agent': 'advanced-api-project'}
    
    # Build URL with pagination
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100}
    if after:
        params['after'] = after
    
    try:
        response = requests.get(url, headers=headers, params=params, 
                              allow_redirects=False)
        
        # Check if request was successful and not redirected
        if response.status_code != 200:
            return
            
        data = response.json()
        
        # Check if data structure is valid
        if 'data' not in data or 'children' not in data['data']:
            return
            
        posts = data['data']['children']
        
        # Count keywords in titles
        for post in posts:
            title = post['data']['title'].lower()
            title_words = title.split()
            
            for word in title_words:
                # Clean word of punctuation
                clean_word = ''.join(char for char in word if char.isalnum())
                if clean_word in word_count:
                    word_count[clean_word] += 1
        
        # Check if there are more pages
        after = data['data'].get('after')
        if after:
            count_words(subreddit, word_list, word_count, after)
        else:
            # Base case: no more pages, print results
            if word_count:
                # Filter out words with 0 count and sort
                filtered_counts = {k: v for k, v in word_count.items() if v > 0}
                sorted_words = sorted(filtered_counts.items(), 
                                    key=lambda x: (-x[1], x[0]))
                
                for word, count in sorted_words:
                    print(f"{word}: {count}")
                    
    except (requests.RequestException, ValueError, KeyError):
        # Handle any request or JSON parsing errors
        return