#!/usr/bin/python3
""" Reddit API """


def top_ten(subreddit):
    """Returns the top 10 hot posts of the subreddit"""
    import requests

    res = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    if res.status_code >= 300:
        print('None')
    else:
        [print(post.get["data"]["title"])
         for post in res.json()["data"]["children"]]
