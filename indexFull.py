from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
# from MyStemmer import MyStemmer
import tweepy
import time,json,re,os, sys
from text_generator import Text_generator
from tweet_poster import tweet_poster

UPLOAD_FOLDER = 'input/tempData/'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/post")
def post():
	consumer_key = "N343ic9LxR6lIdZVaa2R1P0Gm"
	consumer_secret = "oKPXVw45vawk6H6MfEgabgmPENUervO7rV1lk3Qoy1JPQ1ZEMG"

	access_token = "1019130150405828610-fare5LY8Meyj715ijCq5SzIlnDEcDb"
	access_token_secret = "IPDWmVFtiv0S7bYESYQF4AFpNwQ9qtEXUOcF1gtHq9r3o"

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

	return "berhasil"

def lastseen():
	consumer_key = "N343ic9LxR6lIdZVaa2R1P0Gm"
	consumer_secret = "oKPXVw45vawk6H6MfEgabgmPENUervO7rV1lk3Qoy1JPQ1ZEMG"

	access_token = "1019130150405828610-fare5LY8Meyj715ijCq5SzIlnDEcDb"
	access_token_secret = "IPDWmVFtiv0S7bYESYQF4AFpNwQ9qtEXUOcF1gtHq9r3o"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	tweepyapi = tweepy.API(auth)

	#memastikan mention ga dibalas dua kali
	file_name = 'last_seen_id.txt'

	f_read = open(file_name, 'r')
	last_seen_id = str(f_read.read().strip())
	f_read.close()

	mentions = tweepyapi.mentions_timeline(last_seen_id, tweet_mode='extended')

	if len(mentions) != 0 :
		last_seen_id_w = mentions[0].id

		f_write = open(file_name, 'w')
		f_write.write(str(last_seen_id_w))
		f_write.close()

		print("last seen : ",last_seen_id_w)

@app.route("/wakeup")
def wakeup():
	
	lastseen()
	print("PLEASE DON'T SLEEP!")

	return "hai, dipanggil biar ga sleep aja heroku nya"
	

@app.route("/get_data", methods=["GET"])
def get_data():
	text = Text_generator()
	post = tweet_poster()
	data = text.getData()

	kota = data[0]['kota']
	suhu = str(data[0]['suhu']) + " °C"

	if(data[0]['hujan'] == ""):
		hujan = "none"	
	else:
		hujan = str(data[0]['hujan']) + " mm"

	kelembaban = str(data[0]['kelembapan']) + " %"
	angin = data[0]['kec_angin'] +", "+ data[0]['a_angin']
	waktu = data[0]['waktu']

	sentence = text.generator(data)
	# print("dataaa jkahd")
	post.post(sentence)

	return jsonify({
		'kota' :kota,
		'sentence': sentence,
		'waktu': waktu,
		'suhu': suhu,
		'hujan' : hujan,
		'kelembaban' : kelembaban,
		'angin' : angin
		})



if __name__ == "__main__":
    # app.run(port=80,debug=True) #untuk local
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port = port)




# hDVA6ktdC82734

 # cpanel.ukmialkhuarizmi.or.id