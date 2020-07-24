from flask import Flask,render_template,redirect,request
import numpy as np

app = Flask(__name__)


@app.route('/')
def hello():
	return render_template("index.html")
#import caption_it

								
@app.route('/',methods= ['POST'])
def marks():

	if request.method == 'POST':
		f = request.files['userfile']
		path = "./static/{}".format(f.filename)
		f.save(path)

		caption = caption_it.caption_this_image(path)
		
		result_dic = path
		
		return render_template("index.html",your_result = result_dic)
		









