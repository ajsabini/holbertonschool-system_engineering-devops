#!/usr/bin/python3
"""obtain num suscriber for reddit"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers (not active users,
    total subscribers) for a given subreddit  """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0\
                Safari/537.36"}
    subs_count = requests.get(url, headers=headers, allow_redirects=False)

    if subs_count.status_code < 300:
        return subs_count.json()["data"]["subscribers"]
    else:
        return 0
