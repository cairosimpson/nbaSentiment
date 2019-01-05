import json
import math
import os
import sys
from twython import Twython  


class TwitterScraper:

	# There are no private instance variables in python, so it is customary to put a "_" before any variables people shouldn't touch;
	# in that way, they're effectively private.
	_creds = {};
	_queryer = None;


	# Takes in the credentials file's location and reads it in. It then creates an object from the Twython library
	# that is ready to query data.
	def __init__(self, filename):

		# Checks whether the credentials file exists
		if not os.path.exists(filename):
			raise FileNotFoundError(filename + " does not exist. Aborting now.")

		# Read the Credentials file (json) and load them into object
		with open(filename, "r") as file:  
    		_creds = json.load(file)

    	_queryer = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])


    # Takes in a bunch of parameters to query from Twitter API. The parameters are defined here:
    # https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
    #
    # Returns a list of Tweets, that are our Tweet object.
    # Processing inspired by: https://stackabuse.com/accessing-the-twitter-api-with-python/
    def query(self, query="", result_type="popular", geocode="39.8,-95.583068847656,2500km", lang="en", count="100", include_entities=True):

    	tweets = []

    	# Using the keyword arguments passed in, we send out a request to Twitter and iterate through them, returning a list
 		for data in python_tweets.search(**kwargs)['statuses']:
 			tweets.append(Tweet(data))

 		return tweets