from flask import Flask
from flask import jsonify
import pandas as pd
import wikipedia
from google.cloud import language

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello world, this is the project 1 and template for further projects that integrate gcloud'

"""
@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

"""
@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """

@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
