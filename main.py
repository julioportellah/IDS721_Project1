from flask import Flask
from flask import jsonify
import pandas as pd
app = Flask(__name__)

@app.route('/')
def main():
	"""
	The hellow world!
	"""
	return "<p>Hello World, my name is Julio!</p>"

@app.route('/name/<value>')
def name(value):
    	val = {"value": value}
    	return jsonify(val)

@app.route('/html')
def html():
    	"""Returns some custom HTML"""
    	return """
    	<title>This is a Hello World World Page</title>
    	<p>Hello</p>
    	<p><b>World</b></p>
    	"""

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)	
	pass
