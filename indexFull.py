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
	return "berhasil"

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
	# post.post(sentence)
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