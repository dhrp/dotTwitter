import time
from twilio.rest import TwilioRestClient
from django.conf import settings
from main.models import UserProfile
from django.contrib.auth.models import User
from main.models import Tweet, Query
import simplejson
import urllib
from django.core.exceptions import ObjectDoesNotExist

class dotTwitter(object):

    def __init__(self):
        self.user = User.objects.get(pk=1)
        self.keywords = Query.objects.all()

        try:
            self.since_id = Tweet.objects.latest('tweet_id').tweet_id
        except ObjectDoesNotExist:
            self.since_id = 1
        self.phone_number = self.user.userprofile.phone_number
        self.email = self.user.email

    def searchTweets(self, keywords):

        total_set = []

        for keyword in keywords:
            query = '?q={0}&since_id={1}&rpp={2}'.format(keyword.keywords, str(self.since_id), str(100))
            search = urllib.urlopen("http://search.twitter.com/search.json"+query)
            results = simplejson.loads(search.read())["results"]

            if len(results) > 0:
                for result in results:
                    result["keyword"] = keyword.keywords
                    total_set.append(result)
#                    print total_set

        return total_set


    def storeResults(self, tweets):

        for result in tweets: # result is a list of dictionaries

            # convert time from twitter format to python format
            ts = time.strftime('%Y-%m-%d %H:%M:%S+00:00', time.strptime(result['created_at'],'%a, %d %b %Y %H:%M:%S +0000'))

            # strip emoji and other low characters
            text = ''.join([ch for ch in result["text"] if ord(ch) < 0x800])

            tweet = Tweet.objects.create(
                tweet_id = result["id"],
                created_at = ts,
                from_user = result["from_user"],
                from_user_id = result["from_user_id"],
                from_user_name = result["from_user_name"],
                geo = result["geo"],
                iso_language_code = result["iso_language_code"],
                profile_image_url = result["profile_image_url"],
                source = result["source"],
                text = text,
                keyword = result["keyword"]
            )

            if "to_user_id" in result:
                tweet.to_user_id = result["to_user_id"]

            if "ro_user_name" in result:
                tweet.to_user_name = result["to_user_name"]


            tweet.save()

        return "ok. " + str(len(tweets)) + " tweets stored"


    def sendMessage(self, tweets):


        if len(tweets) > 0:
            if len(self.phone_number) > 5:
                twilio_client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

                keyword_string = ''

                for keyword in self.keywords:
                    keyword_string += '"' + str(keyword.keywords) + '" '


                body = "DotTwitter has retrieved " + str(len(tweets)) + " messages with the keywords: " + keyword_string
                try:

                    ## Let's discable sending SMS messages for now
                    # message = twilio_client.sms.messages.create(to=self.phone_number, from_="+14154841479", body=body)
                    pass
                except:
                    return "Twilio error, most likely the receiving number is invalid"

#                print body

                return "one message sent"
            else:
                return "something is wrong with the phone number"

        else:
            return "not sending message"