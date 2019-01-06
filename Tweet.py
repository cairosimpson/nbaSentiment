import json
import math
import sys

# Our class that holds all the information in a Tweet.
class Tweet:

	# Info about the Tweet
	tweet_id = None
	text = ""
	created_at = ""
	hashtags = list()
	user_mentions = list()
	retweet_count = None
	favorite_count = None

	# Info about the user who Tweeted it
	user_id = None
	user_name = ""
	user_description = ""
	user_followers_count = None
	user_created_at = ""
	user_favorites_count = None
	status_count = None
	verified = False


	# Filling hte information of a Tweet
	def __init__(self, data):
		try:
			tweet_id = data['id']
			text = data['text']
			created_at = data['created_at']
			hashtags = data['entities']['hashtags']
			user_mentions = data['entities']['user_mentions']
			user_id = data['user']['id']
			user_name = data['user']['name']
			user_description = data['user']['description']
			user_followers_count = data['user']['followers_count']
			user_created_at = data['user']['created_at']
			user_favorites_count = data['user']['favourites_count']
			status_count = data['user']['statuses_count']
			verified = data['user']['verified']
			reteweet_count = data['user']['retweet_count']
			favorite_count = data['user']['favorite_count']
		except Exception as e:
			print("Passing incomplete data to create a Tweet. Error:")
			print(e)

	# Governs how the Tweet gets converted to a String (for debugging and readibility). "__dict__" is a method that every class has by default
	# which returns a dictionary of all instance variables of the class. We just convert this to a string and return it.
	def __str__(self):
		return str(self.__dict__)

	# Returns whether a tweet is the same as another tweet (that the tweet's ids are the same)
	def __eq__(self, other):
		return self.tweet_id = other.tweet_id

	# Defines how to hash a Tweet (using the id) so that it can be used in hashmaps and sets (which are hashsets)
	def __hash__(self):
        return hash(self.tweet_id)
"""
Exmaple Tweet that is returned by Twitter:
{
    "created_at": "Sun Feb 25 18:11:01 +0000 2018",
    "id": 967824267948773377,
    "id_str": "967824267948773377",
    "text": "From pilot to astronaut, Robert H. Lawrence was the first African-American to be selected as an astronaut by any na… https://t.co/FjPEWnh804",
    "truncated": true,
    "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
            {
                "url": "https://t.co/FjPEWnh804",
                "expanded_url": "https://twitter.com/i/web/status/967824267948773377",
                "display_url": "twitter.com/i/web/status/9…",
                "indices": [
                    117,
                    140
                ]
            }
        ]
    },
    "metadata": {
        "result_type": "popular",
        "iso_language_code": "en"
    },
    "source": "<a href='"https://www.sprinklr.com"' rel='"nofollow"'>Sprinklr</a>",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "user": {
        "id": 11348282,
        "id_str": "11348282",
        "name": "NASA",
        "screen_name": "NASA",
        "location": "",
        "description": "Explore the universe and discover our home planet with @NASA. We usually post in EST (UTC-5)",
        "url": "https://t.co/TcEE6NS8nD",
        "entities": {
            "url": {
                "urls": [
                    {
                        "url": "https://t.co/TcEE6NS8nD",
                        "expanded_url": "http://www.nasa.gov",
                        "display_url": "nasa.gov",
                        "indices": [
                            0,
                            23
                        ]
                    }
                ]
            },
            "description": {
                "urls": []
            }
        },
        "protected": false,
        "followers_count": 28605561,
        "friends_count": 270,
        "listed_count": 90405,
        "created_at": "Wed Dec 19 20:20:32 +0000 2007",
        "favourites_count": 2960,
        "utc_offset": -18000,
        "time_zone": "Eastern Time (US & Canada)",
        "geo_enabled": false,
        "verified": true,
        "statuses_count": 50713,
        "lang": "en",
        "contributors_enabled": false,
        "is_translator": false,
        "is_translation_enabled": false,
        "profile_background_color": "000000",
        "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
        "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
        "profile_background_tile": false,
        "profile_image_url": "http://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/11348282/1518798395",
        "profile_link_color": "205BA7",
        "profile_sidebar_border_color": "000000",
        "profile_sidebar_fill_color": "F3F2F2",
        "profile_text_color": "000000",
        "profile_use_background_image": true,
        "has_extended_profile": true,
        "default_profile": false,
        "default_profile_image": false,
        "following": null,
        "follow_request_sent": null,
        "notifications": null,
        "translator_type": "regular"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": false,
    "retweet_count": 988,
    "favorite_count": 3875,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "lang": "en"
}
"""