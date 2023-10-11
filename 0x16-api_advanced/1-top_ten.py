#!/usr/bin/python3
""" 1. Top Ten """
import requests


def top_ten(subreddit):
    sr = subreddit
    res = requests.get(f"https://www.reddit.com/r/{sr}/hot.json?limit=10",
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)

    if res.status_code != 200:
        print(None)
    else:
        for post in res.json()['data']['children']:
            print(post['data']['title'])
