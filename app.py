# -*- coding: utf-8 -*-
from pymongo import Connection
import json
import tweepy

class AppBot(object):

	def __init__(self, auth):
		self.connection = Connection()
		self.db = self.connection['jobbot']
		self.applicant_collection = self.db['applicants']
		self.tweet_collection = self.db['tweets']

		# setup tweepy auth
		self.api = tweepy.API(auth)

	def save(self, data):
		try:
			json_data = json.loads(data)
			if 'event' in json_data.keys():
				if json_data['event'] == 'follow' and \
					json_data['target']['screen_name'].lower() == 'cust_7':

				    # follow event detected, follow back
				    self.api.create_friendship(json_data['source']['screen_name'])
			elif 'text' in json_data.keys():
				self.tweet_collection.insert(json_data)
				# check if its a job application
				if '#apply' in json_data['text'].lower():
					cur = self.applicant_collection.find({'user.id':json_data['user']['id']})
					if cur.count() > 0:
						# already exists
						pass

					message = "@" + json_data['user']['screen_name'] + " Welcome to stage 2 of the process. Please solve this take home problem and reply here when done. "
					
					# add applicant in database
					applicant = {
						'user': json_data['user']
						}
					# check for job position 
					if '#frontend' in json_data['text'].lower():
						# do something
						applicant['position'] = 'frontend'
						message = message + "http://t.co/frontend"
						
					elif '#devops' in json_data['text'].lower():
						# do something
						applicant['position'] = 'devops'
						message = message + "http://t.co/devops"
						
					elif '#python' in json_data['text'].lower():
						# do something
						applicant['position'] = 'python'
						message = message + "http://t.co/python"
					
					self.applicant_collection.insert(applicant)

					# send a welcome tweet
					
					self.api.update_status(status=message, in_reply_to_status_id=json_data['id'])
					
		except Exception,e:
			print e
			pass


