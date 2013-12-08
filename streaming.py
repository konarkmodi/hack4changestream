# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from app import AppBot

# The consumer key and secret
consumer_key=
consumer_secret=


# access token
access_token="898663117-v2KJDqXcIJcx6lgsmczywQ2FIeNRcq8aGPB9fpJD"
access_token_secret="CnbI7MbbML7T9TX6LEJzE0J0AVOpuyY0BtY6p80E"


# instantiating the App bot
bot = None

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print data
        bot.save(data)
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    bot = AppBot(auth)
    stream = Stream(auth, l)
    stream.userstream()
