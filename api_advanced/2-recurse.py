#!/usr/bin/python3
"""
Function that queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    
    Args:
        subreddit (str): The subreddit to search
        hot_list (list): List to store the titles
        after (str): Parameter for pagination
    
    Returns:
        list: List of titles or None if invalid subreddit
    """
    if hot_list is None:
        hot_list = []
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python:subreddit.posts:v1.0 (by /u/testuser)"}
    params = {"limit": 100}
    
    if after:
        params["after"] = after
    
    try:
        response = requests.get(url, headers=headers, params=params,
                              allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            
            if not posts:
                return hot_list if hot_list else None
            
            for post in posts:
                hot_list.append(post["data"]["title"])
            
            after = data.get("data", {}).get("after")
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception:
        return None
