#!/usr/bin/python3
"""
Function to query Reddit API for subreddit subscriber count
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit
        
    Returns:
        int: Number of subscribers, or 0 if invalid subreddit
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/temp_user)'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except (requests.RequestException, KeyError, ValueError):
        return 0
