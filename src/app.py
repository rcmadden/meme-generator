from IngestEngine import Ingestor

from flask import Flask, render_template

app = Flask(__name__)

def setup():
    """ Load all resources """
    path_prefix = '/Users/russiam/_Dev/udacity-meme-generator/meme-generator/src'
    # quote_files = [path_prefix + '/_data/DogQuotes/DogQuotesCSV.csv']

    quote_files = [
                    path_prefix + '/_data/DogQuotes/DogQuotesTXT.txt',
                   path_prefix + '/_data/DogQuotes/DogQuotesDOCX.docx',
                   path_prefix + '/_data/DogQuotes/DogQuotesPDF.pdf',
                   path_prefix + '/_data/DogQuotes/DogQuotesCSV.csv'
                   ]
    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for i in range(len(quote_files)):
        print(quote_files[i])
        quotes.append(Ingestor.parse(quote_files[i]))

    # images_path = "./_data/photos/dog/"
    images_path = path_prefix + "/_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = None
    print(quotes)
    return quotes, imgs

# quotes, imgs = setup()
quotes = setup()
# quotes = CSVIngestor.parse(quote_files[0])

@app.route("/")
def hello_world():
    return "<p>Hello, from Russia!</p>"

# @app.route("/")
# def meme_rand():
#     quotes = CSVIngestor.parse(quote_files[0])
#     path = quotes[0]
#     return render_template('meme.html', path=path)

# path_prefix = '/Users/russiam/_Dev/udacity-meme-generator/meme-generator/src'
# quote_files = [path_prefix + '/_data/DogQuotes/DogQuotesCSV.csv']
# TODO:
# [x] iterate over quote_files
# [x] refactor Importer
# [x] call the Importer
# [] refactor TextIngestor to parse files
# [] refactor PDFIngestor to parse files


# print(CSVIngestor.parse(quote_files[0]))

# quotes = CSVIngestor.parse(quote_files[0])
hello_world()