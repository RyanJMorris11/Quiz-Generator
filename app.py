from flask import Flask, render_template, request, redirect, url_for
from lib.Scraper import Scraper
from lib.Database import Database
import tensorflow as tf
import requests
import pymysql
import _thread
import time

app = Flask(__name__)

@app.route("/")
def index():
	
	return render_template("index.html")
	
@app.route("/exam")
def exam():
	keyword = request.args.get('keyword')
	db = Database()
	questions = db.selectQuestions(keyword)
	return render_template("exam.html", questions=questions, keyword=keyword)
	
	
@app.route("/quizlet", methods=['GET', 'POST'])
def quizlet_search():
	if request.method == 'POST': 
		search = request.form.get('search')
		try:
			_thread.start_new_thread( scrape_quizlet, (search,) )
		except:
			print( "cannot create a new thread")
			

		return redirect(url_for('exam', keyword=search))
		
	
	return "you were searching"
	
def scrape_quizlet(search):
	sc = Scraper()
	data = sc.scan_and_scrape(search)
	
    
	
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=80)
	