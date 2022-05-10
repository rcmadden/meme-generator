import os
import random
from urllib import response
import requests
from flask import Flask, render_template, abort, request, redirect, url_for
from markupsafe import escape
from PIL import Image
from IngestEngine import Ingestor
from MemeGenerator import MemeEngine


app = Flask(__name__)
meme = MemeEngine('./static/tmp')


def setup():
    """ Load all resources """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = None
    quote = None

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    out_path = './static/tmp.'

    try:
        os.remove(out_path + 'jpg')
    except:
        print('no file exists')

    try:
        os.remove(out_path + 'png')
    except:
        'no file to remove'

    img_url = request.form['image_url']
    out_file = out_path + img_url.split('.')[-1]
    response = requests.get(img_url)

    # try:
    #     with Image.open(response) as im:
    #         print('verify')
    #         im.verify()
    # except:
    #     'invalid image'
    # return

    with open(out_file, 'wb') as img:
        print('write')
        img.write(response.content)

    body = request.form['body']
    author = request.form['author']

    # if body == '':
    #     body = 'To be or not to be'
    # if author == '':
    #     author = 'Shakespeare'

    path = meme.make_meme(out_file, body, author)
    # TODO: handle invalid url/img

    return render_template('meme.html', path=path)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/<name>/')
def index(name):
    name = escape(name)
    return render_template('page_not_found.html', name=name)


if __name__ == "__main__":
    app.run()
