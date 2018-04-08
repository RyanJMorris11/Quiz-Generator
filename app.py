from flask import Flask, render_template, request, redirect, url_for
from lib.Scraper import Scraper
from lib.Database import Database
import tensorflow as tf
import requests
import pymysql

app = Flask(__name__)

@app.route("/")
def index():

	return render_template("index.html")
	
	
@app.route("/quizlet", methods=['GET', 'POST'])
def quizlet_search():
	if request.method == 'POST': 
		search = request.form.get('search')
		sc = Scraper()
		data = sc.scan_and_scrape(search)
		#return redirect(url_for('index'))
		
	
	return "you were searching"
	
    
	
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=80)
	