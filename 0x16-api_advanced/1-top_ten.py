#!/usr/bin/python3
"""
function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyBot/1.0 (your_username)"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            print(title)
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
    else:
        print(f"Error: {response.status_code}")
