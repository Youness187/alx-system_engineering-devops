#!/usr/bin/python3
"""
 function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
       and returns the number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
                     v1.0.0 (by /u/dayouness)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
