#!/usr/bin/python3
"""Reddit API"""


def number_of_subscribers(subreddit):
    """Returns the number of subscribers in a subreddit"""
    import requests

    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    if res.status_code >= 300:
        return 0

    return res.json()["data"]["subscribers"]
