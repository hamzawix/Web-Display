#!/usr/bin/ python3.5
from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/temp')
def temp():
	n = random.random() * 100
	return str(n)

@app.route('/carb')
def carb():
	k = random.random() * 100
	return str(k)

@app.route('/vit')
def vit():
	v = random.random() * 100
	return str(v)


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)