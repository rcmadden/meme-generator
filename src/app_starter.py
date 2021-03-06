import random
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from MemeGenerator import MemeEngine

from IngestEngine import IngestInterface
from QuoteEngine import QuoteModel


app = Flask(__name__)
# Create this directory./static
meme = MemeEngine('./static')


def setup():
    """ Load all resources """
    path_prefix = '/Users/russiam/_Dev/udacity-meme-generator/meme-generator/src'
    # quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
    #                './_data/DogQuotes/DogQuotesDOCX.docx',
    #                './_data/DogQuotes/DogQuotesPDF.pdf',
    #                './_data/DogQuotes/DogQuotesCSV.csv']

    quote_files = [path_prefix + '/_data/DogQuotes/DogQuotesTXT.txt',
                   path_prefix + '/_data/DogQuotes/DogQuotesDOCX.docx',
                   path_prefix + '/_data/DogQuotes/DogQuotesPDF.pdf',
                   path_prefix + '/_data/DogQuotes/DogQuotesCSV.csv']
    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = None

    # images_path = "./_data/photos/dog/"
    images_path = path_prefix + "/_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = None

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = None
    quote = None
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path = None

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
