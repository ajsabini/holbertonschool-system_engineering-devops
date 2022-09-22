#!/usr/bin/python3
"""task 1"""
import requests


def top_ten(subreddit):
    """ print title of 10 hot posts """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleW\
            ebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    subs_hot = requests.get(url, headers=headers)

    if subs_hot.status_code < 300:
        data = subs_hot.json()
        hot_posts = data['data']['children']
        for post in hot_posts[:10]:
            print(post['data']['title'])

    else:
        print("None")
