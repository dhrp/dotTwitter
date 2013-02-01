#!/home/dotcloud/env/bin/python

import sys
sys.path.append("/Users/thatcher/Develop/dotTwitter")
sys.path.append("/Users/thatcher/Develop/dotTwitter/dotTwitter")

sys.path.append("/home/dotcloud")
sys.path.append("/home/dotcloud/current")

import os
os.environ["DJANGO_SETTINGS_MODULE"] = "dotTwitter.settings"

#from django.db import models
from datetime import datetime
#from django.conf import settings
#import urllib
#import urlparse
#import simplejson
#from main.models import Tweet
from helpers.dottwitter import dotTwitter


now = str(datetime.now())

dot = dotTwitter()

keywords = dot.keywords
message = ""
tweets = dot.searchTweets(keywords)
status = dot.storeResults(tweets)

# We are now disabling the actual sending of messages so we can aggregate climate change keywords
#message = dot.sendMessage(tweets)

print tweets
print status
print message


with open("output.txt", "a") as myfile:
    myfile.write(now + " appended text \n")

