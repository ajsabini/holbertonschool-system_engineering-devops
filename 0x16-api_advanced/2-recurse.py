#!/usr/bin/python3
"""task 0"""
import requests


def recurse(subreddit, hot_list=[], after="inicio"):
	""" returns the number of subscribers (not active users,
    total subscribers) for a given subreddit  """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headersUA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

	if after != "inicio":
		url = url + "?after={}".format(after)
		
	
	subs_hot = requests.get(url,headers=headersUA,allow_redirects=False)
	data = subs_hot.json()
	
	hotTitles = data.get("data", {}).get("children", [])

	if not hotTitles:
		return None

	for ht in hotTitles:
		hot_list.append(ht["data"]["title"])

	after = data["data"]["after"]

	if not after:
		return hot_list

	return (recurse(subreddit, hot_list, after))
