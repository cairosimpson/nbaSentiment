import json
import math
import sys
import json
from Tweet import Tweet
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import wordpunct_tokenize

# Actual object that holds all the Tweets and is a list
# You can call this with "import Dataset; ds = Dataset.Dataset(list_of_tweets)"
class DataSet:
	_data = []

	def __init__(self, tweets):
		_data = tweets

	def __add__(self, other): 
		return Dataset(self._data + other._data)

	# Inefficient, but it removes the data from self that is in "other". This is largely an unecessary function
	# but also because it's so easy to do, I use it.
	def __sub__(self, other):

		# Using set()'s functionality of subtraction (it removes all the elements of the second from the first), I define
		# subtraction the same way
		return Dataset(list(set(self._data) - set(other._data)))

	# Returns a generator in Python, which acts as an iterator.
	# Now you can use "for tweet in DataSet"
	def __iter__(self):
   		for tweet in _data:
      		yield tweet

	# TODO: @Cairo to implement
	def __len__(self):
		return None

	# TODO: @Cairo to implement using tweet's ids
	def __contains__(self, tweet):
		return None

# ================================================================================================================
# All public methods that will be accessed upon import of this file outside of the Dataset class
# You can call these with "import Dataset; stemmed_text = Datset.stem(text)"
# ================================================================================================================

# Initializes a stemmer; this takes a second or two
_stemmer = SnowballStemmer("english")

# Returns a stemmed version of a string
def stem(text, ignore_stopwords=True):
	return _stemmer.stem(tweet, ignore_stopwords=ignore_stopwords)

# Tokenizes a string and returns a list of all the tokens
def tokenize(text):
	return wordpunct_tokenize(text)