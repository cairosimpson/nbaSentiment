import json
import math
import sys
import pandas as pd
from twython import Twython  


class TwitterScraper:

	def __init__(self, filename):
		print "a"

		with open(filename, "r") as file:  
    		creds = json.load(file)


    def publicMethod():
    	print "b"