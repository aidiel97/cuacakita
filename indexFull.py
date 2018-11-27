from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
# from MyStemmer import MyStemmer
import time,json,re,os
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

@app.route("/get_data", methods=["GET"])
def get_data():

	text = Text_generator()
	post = tweet_poster()
	data = text.getData()

	suhu = str(data[0]['suhu']) + " °C"
	hujan = str(data[0]['hujan']) + " mm"
	kelembaban = str(data[0]['kelembapan']) + " %"
	angin = data[0]['kec_angin'] +", "+ data[0]['a_angin']
	waktu = data[0]['waktu']

	sentence = text.generator(data)
	# print("dataaa jkahd")
	post.post(sentence)
	return jsonify({
		'sentence': sentence,
		'waktu': waktu,
		'suhu': suhu,
		'hujan' : hujan,
		'kelembaban' : kelembaban,
		'angin' : angin
		})



if __name__ == "__main__":
    app.run(port=80,debug=True)