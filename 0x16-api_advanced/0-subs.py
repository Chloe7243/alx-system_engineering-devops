#!/usr/bin/python3
""" 0. How many subs? """
import requests


def number_of_subscribers(subreddit):
    res = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    print(res.status_code)
    return 0 if res.status_code != 200 else res.json()['data']['subscribers']
