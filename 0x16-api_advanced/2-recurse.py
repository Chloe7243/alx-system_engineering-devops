#!/usr/bin/python3
""" 2. recurser """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ recursion """
    sr = subreddit
    res = requests.get(f"https://www.reddit.com/r/{sr}/hot.json?after={after}",
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)

    if res.status_code >= 400:
        return None

    d = res.json()
    result = hot_list + [p['data']['title'] for p in d['data']['children']]
    if not d['data']['after']:
        return result
    return recurse(subreddit, result, d['data']['after'])
