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
        	text_gen = Text_generator()
        	data = text_gen.getCData(ans)
        	sentence = text_gen.generator(data)

        	print('menemukan tweet yang harus dibalas!', flush=True)
        	print('respond tweet...', flush=True)

        	api.update_status('Hai! @' + mention.user.screen_name + 
            	" " + sentence, mention.id)

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=25)
def timed_job():
    print('This job is run every 0.25 minutes.')
    reply_to_tweets()


# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')

sched.start()