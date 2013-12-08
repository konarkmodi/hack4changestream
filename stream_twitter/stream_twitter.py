from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from config import *
from pymongo import MongoClient
import json

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=key
consumer_secret=secret

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=access_key
access_token_secret=access_secret

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

class CustomStreamListener(StreamListener):
    def __init__(self, api):
        self.api = api
        super(StreamListener, self).__init__()

        self.db = MongoClient("mongodb://user:hack4change@linus.mongohq.com:10000/hack4change").hack4change

    def on_data(self, tweet):
        self.db.test_tweets.insert(json.loads(tweet))

    def on_error(self, status_code):
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    #l = CustomStreamListener(auth)

    stream = Stream(auth, l)
    stream.filter(track=["don't you bitch"])
