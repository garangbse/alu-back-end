# alu-back-end

## API Advanced Scripts Overview

This project contains a collection of advanced Python scripts in the `api_advanced/` folder that interact with various APIs to demonstrate advanced API usage patterns and data handling techniques:

### Scripts Description

**0-subs.py**
- Fetches the number of subscribers for a given subreddit using the Reddit API
- Takes a subreddit name as a function parameter
- Returns the subscriber count or 0 if the subreddit is invalid
- Usage: Function call with subreddit name as argument

**1-top_ten.py**
- Retrieves and prints the titles of the first 10 hot posts for a given subreddit
- Uses the Reddit API to fetch hot posts in JSON format
- Prints "None" if the subreddit is invalid or has no posts
- Usage: Function call with subreddit name as argument

**2-recurse.py**
- Recursively fetches all hot article titles for a given subreddit using the Reddit API
- Implements pagination to retrieve all posts, not just the first page
- Returns a list of all hot post titles or None if subreddit is invalid
- Usage: Recursive function call with subreddit name as argument

**3-count.py**
- Recursively parses all hot article titles in a subreddit and counts keyword occurrences
- Takes a subreddit name and list of keywords as parameters
- Prints keyword counts in descending order, alphabetically sorted for ties
- Case-insensitive keyword matching with whole word boundaries
- Usage: Function call with subreddit name and keyword list as arguments

All scripts interact with the Reddit API and include proper error handling, HTTP status code validation, and respect for API rate limits and best practices.
