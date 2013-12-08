from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from config import *
import json

def send_reply(tweetID,screen_name):
	try:
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api = API(auth)
		### at this point I've grabbed the tweet and loaded it to JSON...
		status_message = "@%s You are not supposed to use such words. @stophatebot " % (screen_name)
		api.update_status(status_message, tweetID)
	except Exception, e:
		print e

if __name__ == '__main__':
	send_reply('409521572102168576','Austin2xx')



