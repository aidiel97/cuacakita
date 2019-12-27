import tweepy
from RequestAPI import RequestAPI

class tweet_poster:
	def post(self, sentence):
		consumer_key = "N343ic9LxR6lIdZVaa2R1P0Gm"
		consumer_secret = "oKPXVw45vawk6H6MfEgabgmPENUervO7rV1lk3Qoy1JPQ1ZEMG"

		access_token = "1019130150405828610-fare5LY8Meyj715ijCq5SzIlnDEcDb"
		access_token_secret = "IPDWmVFtiv0S7bYESYQF4AFpNwQ9qtEXUOcF1gtHq9r3o"

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		tweepyapi = tweepy.API(auth)
		# text_gen = Text_generator()

		# sentence = text_gen.cleanedData()
		# text_gen.cleanedData()

		tweepyapi.update_status(sentence)
		print("tweet berhasil di post :", sentence)
