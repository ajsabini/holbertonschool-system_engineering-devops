#!/usr/bin/python3
"""task 1"""
import requests


def top_ten(subreddit):
    """ print title of 10 hot posts """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    hedaers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
                (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    subs_hot = requests.get(url, headers=headers, allow_redirects=False)

    if subs_hot.status_code == 200:
        data = subs_hot.json()
        hot_posts = data["data"]["children"]
        for post in hot_posts[:10]:
            print(post["data"]["title"])
    else:
        print("None")
