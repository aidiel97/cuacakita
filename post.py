from apscheduler.schedulers.blocking import BlockingScheduler
import tweepy
import time,json,re,os, sys
from text_generator import Text_generator
from tweet_poster import tweet_poster

def post():
	consumer_key = "k2HFUcJA2CMcb2JwWnFYXmwGs"
	consumer_secret = "ZnedSsVh8nAJrhkwMbyITCJsTCP4D4a8VO2zhr7Qj5kcya1UN1"

	access_token = "1019130150405828610-tjzmuDjAFXBvwftL6ugevFtd1vPhys"
	access_token_secret = "e7zUjaCimnYKQtlrRu75ynXupUQu4NkTrQmN3wBuM7YPO"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	tweepyapi = tweepy.API(auth)

	text_gen = Text_generator()
	data = text_gen.getData()
	sentence = text_gen.generator(data)

	tweepyapi.update_status(sentence)
	print("tweet berhasil di post :", sentence)
	
	#memastikan mention ga dibalas dua kali
	file_name = 'last_seen_id.txt'

	f_read = open(file_name, 'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()

	mentions = tweepyapi.mentions_timeline(last_seen_id, tweet_mode='extended')

	if len(mentions) != 0 :
		last_seen_id_w = mentions[0].id

		f_write = open(file_name, 'w')
		f_write.write(str(last_seen_id_w))
		f_write.close()

		print("last seen : ",last_seen_id_w)

#for test
# while True:
#     post()
#     time.sleep(60)


#for heroku
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=0.5)
def timed_job():
    print('post every 1 minutes.')
    reply_to_tweets()

sched.start()