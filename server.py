#!/usr/bin/ python3.5
from flask import Flask, render_template, jsonify
import random
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/charts')
def charts():
	return render_template("charts.html")

@app.route('/timed_data')
def timed_data():

	mydict = {"temp":[], "carb":[], "vit":[]}
	datafile = csv.reader(open(r"data.csv", "rt"))
	for row in datafile:
		mydict["temp"].append(row[0])
		mydict["carb"].append(row[1])
		mydict["vit"].append(row[2])

	return jsonify(mydict)

@app.route('/data')
def data():
	t = round(random.random() * 100, 2)
	c = round(random.random() * 100, 2)
	v = round(random.random() * 100, 2)

	l = [t,c,v]

	with open(r"data.csv", 'a') as f:
		w = csv.writer(f)
		w.writerow(l)

	with open(r"time.csv", 'a') as f:
		w = csv.writer(f)
		w.writerow(["{}:{}:{}".format(datetime.now().hour, datetime.now().minute, datetime.now().second)])

	return jsonify({'t': int(t),
					'c': int(c),
					'v': int(v)})

if __name__ == '__main__':

	r = open(r"data.csv", "w+")
	r.close()
	
	r = open(r"time.csv", "w+")
	r.close()
	app.run(host="localhost", port=5000)