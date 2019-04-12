from flask import Flask,render_template,request,url_for,redirect,session,jsonify
import sqlite3 as sq
import hashlib
import random
# from chat import Bot
# k = Bot()

app=Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')


@app.route("/about")
def about():
	return render_template('about.html')


@app.route("/chatbot")
def chatbot():
	# k.refresh()
	return render_template('chat.html')



@app.route('/ask', methods = ["POST"])
def ask():
	msg  = request.form['messageText']
	#ans  = k.response(msg)
	ans  = 'ChatBot Response'
	return jsonify({'status':'OK','answer':ans})



if __name__=="__main__":
	app.run(port=5000,debug=True)
