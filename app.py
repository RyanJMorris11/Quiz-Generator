from flask import Flask, render_template, request, redirect, url_for
from lib.Scraper import Scraper
import tensorflow as tf
import requests
import pymysql

app = Flask(__name__)

@app.route("/")
def index():

	conn = pymysql.connect(host='localhost', user='root', passwd='theBois', db='Question_Database')
	cur = conn.cursor()
	cur.execute("SELECT * FROM Test_Questions")
	for response in cur:
		print(response)
	cur.close()
	conn.close()
	return render_template("index.html")
	
	
@app.route("/quizlet", methods=['GET', 'POST'])
def quizlet_search():
	if request.method == 'POST': 
		search = request.form.get('search')
		sc = Scraper()
		data = sc.scan_and_scrape(search)
		#return redirect(url_for('index'))
		return str(data)
	
	return "you were searching"
	
@app.route('/query-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None

    return '''<h1>The language value is: {}</h1>'''.format(language)
    
	
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=80)
	