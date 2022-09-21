#!/usr/bin/python3
"""task 0"""
import requests


def top_ten(subreddit):
	""" returns the number of subscribers (not active users, total subscribers) for a given subreddit  """

	subs_hot = requests.get("https://www.reddit.com/r/{}/hot.json"
                                  .format(subreddit),headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"},allow_redirects=False)

	if subs_hot.status_code == 200:
		data = subs_hot.json()
		hot_posts = data["data"]["children"]
		for post in hot_posts[:10]:
			print(post["data"]["title"])
	else:
		print("None")
