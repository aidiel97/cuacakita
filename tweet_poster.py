import tweepy
from RequestAPI import RequestAPI
import time

class tweet_poster:
	def post(self, sentence):
		consumer_key = "k2HFUcJA2CMcb2JwWnFYXmwGs"
		consumer_secret = "ZnedSsVh8nAJrhkwMbyITCJsTCP4D4a8VO2zhr7Qj5kcya1UN1"

		access_token = "1019130150405828610-tjzmuDjAFXBvwftL6ugevFtd1vPhys"
		access_token_secret = "e7zUjaCimnYKQtlrRu75ynXupUQu4NkTrQmN3wBuM7YPO"

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		tweepyapi = tweepy.API(auth)
		# text_gen = Text_generator()

		# sentence = text_gen.cleanedData()
		# text_gen.cleanedData()

		tweepyapi.update_status(sentence)
		print("tweet berhasil di post :", sentence)

	def postm(self):
		consumer_key = "k2HFUcJA2CMcb2JwWnFYXmwGs"
		consumer_secret = "ZnedSsVh8nAJrhkwMbyITCJsTCP4D4a8VO2zhr7Qj5kcya1UN1"

		access_token = "1019130150405828610-tjzmuDjAFXBvwftL6ugevFtd1vPhys"
		access_token_secret = "e7zUjaCimnYKQtlrRu75ynXupUQu4NkTrQmN3wBuM7YPO"

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		INTERVAL = 60
		tweepyapi = tweepy.API(auth)
		# text_gen = Text_generator()

		# data = text_gen.getData()
		# sentence = text_gen.generator(data)
		a = 35
		while True:
			tweepyapi.update_status(a)
			print("tweet berhasil di post :", a)
			a+=1
			time.sleep(INTERVAL)

p = tweet_poster()
p.postm()