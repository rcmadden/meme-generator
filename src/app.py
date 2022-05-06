from flask import Flask, render_template
import os
import random
from IngestEngine import Ingestor
from MemeGenerator import MemeEngine


app = Flask(__name__)
meme = MemeEngine('./static')

def setup():
    """ Load all resources """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    images = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]
   
    return quotes, imgs

quotes, imgs = setup()
# print(quotes, imgs)

@app.route("/")
def hello_world():
    return "<p>Hello, from Russia with love!</p>"

# @app.route("/")
# def meme_rand():
    # img = random.choice(imgs)

#     quotes = CSVIngestor.parse(quote_files[0])
#     path = quotes[0]
#     return render_template('meme.html', path=path)

@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = None
    quote = None

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    img = random.choice(imgs)
    # 2. select a random quote from the quotes array
    quote = random.choice(quotes)
    print(len(quotes))
    print(quote.body)
    print(quote.author)
    # path = meme.make_meme(img, quote.body, quote.author)
    # print("IMAGE, QUOTE.BODY, QUOTE.AUTHOR")
    # print(img, quote.body, quote.author)
    # return render_template('meme.html', path=path)


# TODO:
# [x] iterate over quote_files
# [x] refactor Importer
# [x] call the Importer
# [] refactor TextIngestor to parse files
# [] refactor PDFIngestor to parse files


# print(CSVIngestor.parse(quote_files[0]))

# quotes = CSVIngestor.parse(quote_files[0])
hello_world()
meme_rand()

# if __name__ == "__main__":
#     app.run()