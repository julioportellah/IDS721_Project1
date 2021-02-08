from flask import Flask
from flask import jsonify
import pandas as pd
import wikipedia
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
    	<title>This is a Hello World</title>
    	<p>Hello</p>
    	<p><b>World!!!</b></p>
    	"""
@app.route('/pandas')
def pandas_sugar():
    	df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    	return jsonify(df.to_dict())

@app.route('/wikipedia/<company>')
def wikipedia_route(company):
	try:
		#from google.cloud import language
    		#return "Succeed"
		result = wikipedia.summary(company, sentences=10)
		return result
	except Exception as ex:
		return 'The word "{}" is not valid'.format(company)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)	
	pass
