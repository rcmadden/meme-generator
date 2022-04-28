from IngestEngine import DocxIngestor, CSVIngestor

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

path_prefix = '/Users/russiam/_Dev/udacity-meme-generator/meme-generator/src'
quote_files = [path_prefix + '/_data/DogQuotes/DogQuotesCSV.csv']


print(CSVIngestor.parse(quote_files[0]))