from apscheduler.schedulers.blocking import BlockingScheduler
import tweepy
import time
import re
from translator import Translate
from text_generator import Text_generator

print('Reply BOT!', flush=True)

consumer_key = "k2HFUcJA2CMcb2JwWnFYXmwGs"
consumer_secret = "ZnedSsVh8nAJrhkwMbyITCJsTCP4D4a8VO2zhr7Qj5kcya1UN1"

access_token = "1019130150405828610-tjzmuDjAFXBvwftL6ugevFtd1vPhys"
access_token_secret = "e7zUjaCimnYKQtlrRu75ynXupUQu4NkTrQmN3wBuM7YPO"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# mentions = api.mentions_timeline()

# for mention in mentions:
# 	print( str(mention.id) +" - "+ mention.text)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name): #melihat idtweet terakhir yang distore, mencegah, tweet dibalas duakali
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name): #setelah dibaca tweet mention yg terakhir, maka idtweet akan dicatat di file 'last_seen_id.txt'
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # id last seen testing : 1112619279025725441
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions): #supaya membaca perulangannya terbalik..
    #biasanya list mention di timline dibaca dari yg terakhir dahulu, supaya terurut, maka dibalik
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        tweet = mention.full_text
        tlow = tweet.lower()
        city = re.findall(r"#(\w+)", tlow)

        translate = Translate()
        ans = translate.kamusDaerah(city)
        print(ans)

        # if '#hai' in mention.full_text.lower():
        if ans != "no":
        	print('menemukan tweet yang harus dibalas!', flush=True)
        	
        	text_gen = Text_generator()
        	data = text_gen.getCData(ans)
        	sentence = text_gen.generator(data)

        	print('respond tweet...', flush=True)

        	api.update_status('Hai! @' + mention.user.screen_name + 
            	" " + sentence, mention.id)

        else :
        	api.update_status('Hai! @' + mention.user.screen_name + 
				"sayang sekali " + city + 
				" bukanlah salah satu nama daerah di Indonesia :(\nCuki hanya dibuat untuk kamu yang ingin tau prakiraan cuaca di Indonesia saja\n\nAyo coba yang lain", mention.id)

def post():
	print("POSTING JOB")
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

def post_job():
    print('post every 3 hour.')
    post()

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=0.25)
def timed_job():
    print('This job is run every 0.25 minutes.')
    reply_to_tweets()

sched.add_job(post_job, 'cron', hour='0,3,6,9,12,15,18,21')

sched.start()