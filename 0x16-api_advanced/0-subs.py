#!/usr/bin/python3
"""
 function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API
    and returns the number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"User-Agent": "MyCustomUserAgent/1.0"}
    response = requests.get(url, allow_redirects=False, headers=headers)

    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    return data
