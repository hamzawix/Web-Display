#!/usr/bin/ python3.5
from flask import Flask, render_template, jsonify
import random
app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/data')
def data():
	t = random.random() * 100
	c = random.random() * 100
	v = random.random() * 100

	return jsonify({'t': int(t),
					'c': int(c),
					'v': int(v)})

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)