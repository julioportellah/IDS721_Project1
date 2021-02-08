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

@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

@app.route('/wikipedia/<company>')
def wikipedia_route(company):
    try:
        result = wikipedia.summary(company, sentences=10)

        client = language.LanguageServiceClient()
        document = language.Document(
            content=result,
            type_=language.Document.Type.PLAIN_TEXT)
        encoding_type = language.EncodingType.UTF8
        entities = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type}).entities
        return str(entities)  
    except Exception as ex:
        return "The entered text "{}" didn't work".format(company)
    """
    # Imports the Google Cloud client library
    from google.cloud import language
    result = wikipedia.summary(company, sentences=10)

    client = language.LanguageServiceClient()
    document = language.Document(
        content=result,
        type_=language.Document.Type.PLAIN_TEXT)
    encoding_type = language.EncodingType.UTF8
    entities = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type}).entities
    return str(entities)
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
