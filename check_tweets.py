#!/usr/bin/env python3

import tweepy

API_key = ""
API_secret = ""
access_token = ""
access_token_secret = ""

def Api():
	auth = tweepy.OAuthHandler(API_key, API_secret)
	auth.set_access_token(access_token, access_token_secret)

	return tweepy.API(auth)

def get_tweets():
	api = Api()
	try:
		th = input("Enter twitter's handle: ")
		tweets = tweepy.Cursor(api.user_timeline, th).items(5)
		print("--"*50)

		for tweet in tweets:
			print("--> %s" % tweet.text)
			print("--"*50)

	except tweepy.error.TweepError:
		print("'%s' doesn't exist" % th)

if __name__ == "__main__":
	get_tweets()