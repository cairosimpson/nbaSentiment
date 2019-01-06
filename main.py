import json
import math
import sys
import TwitterScraper

# Create Scraper w/ credential file
ts = TwitterScraper.TwitterScraper("./credentials.py")

tweets = ts.query("nba")

for tweet in tweets:
	print(tweet.text)

data = DataSet(tweets)
print "a"
