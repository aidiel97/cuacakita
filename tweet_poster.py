import tweepy
from RequestAPI import RequestAPI
from text_generator import Text_generator

class tweet_poster:
	def post(self):
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

t = tweet_poster()
t.post()