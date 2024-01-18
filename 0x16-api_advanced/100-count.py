#!/usr/bin/python3
""" 2. recurser """
import requests


def recurse(subreddit, word_list, titles={}, after=None):
    """ recursion """
    sr = subreddit
    res = requests.get(f"https://www.reddit.com/r/{sr}/hot.json?after={after}",
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)

    if res.status_code >= 400:
        return None

    d = res.json()
    result = titles
    for p in d['data']['children']:
        for word in word_list:
            if word in p['data']['title']:
                result[word] +=
    if not d['data']['after']:
        return result.sort()
    return recurse(subreddit, result, d['data']['after'])
