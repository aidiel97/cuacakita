from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'input/tempData/'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

file_name = 'last_seen_id.txt'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def main():
	f_read = open(file_name, 'r')
	last_seen_id = str(f_read.read().strip())
	f_read.close()
	return last_seen_id

@app.route("/post/<last_seen_id>", methods=['GET'])
def post(last_seen_id):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return last_seen_id

if __name__ == "__main__":
    app.run(port=80,debug=True) #untuk local
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host="0.0.0.0", port = port)




# hDVA6ktdC82734

 # cpanel.ukmialkhuarizmi.or.id