#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    
    Args:
        subreddit (str): The subreddit name
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'MyRedditApp/1.0'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            for i in range(min(10, len(posts))):
                print(posts[i]['data']['title'])
        else:
            print("None")
    except (requests.RequestException, KeyError, ValueError):
        print("None")