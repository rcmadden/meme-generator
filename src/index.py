# from crypt import methods
# from http.client import InvalidURL
from logging import exception
import os
import random
# from urllib import response
import requests
# from requests.exceptions import MissingSchema
from flask import Flask, render_template, abort, request, redirect, url_for
from markupsafe import escape
# from PIL import Image
from IngestEngine import Ingestor
from MemeGenerator import MemeEngine


app = Flask(__name__)
os.chdir('/home/russiam/meme-generator/src') # set pythonanywhere cwd
meme = MemeEngine('./static/tmp')


def setup():
    """ Load all resources """
    # quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
    #                './_data/DogQuotes/DogQuotesDOCX.docx',
    #                './_data/DogQuotes/DogQuotesPDF.pdf',
    #                './_data/DogQuotes/DogQuotesCSV.csv']

    quote_files = ['./_data/SkyQuotes/SkyQuotesTXT.txt',
                   './_data/SkyQuotes/SkyQuotesDOCX.docx',
                   './_data/SkyQuotes/SkyQuotesPDF.pdf',
                   './_data/SkyQuotes/SkyQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    # images = "./_data/photos/dog/"
    images = "./_data/photos/skye/"

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

    # TODO: 1. remove file method? repeated code in MemeEngine.py
    # 2. handle exception explicitly

    try:
        os.remove(out_path + 'jpg')
    except exception as e:
        print('no jpg file exists:', e)

    try:
        os.remove(out_path + 'png')
    except exception as e:
        print('no png file to remove', e)

    img_url = request.form['image_url']
    image_type = img_url.split('.')[-1]
    if image_type == 'jpg' or image_type == 'png':
        out_file = out_path + image_type
        response = requests.get(img_url)
    else:
        msg = 'url must contain .png or .jpg'
        return render_template('meme_form.html')

    # try:
    #     with Image.open(response) as im:
    #         print('verify')
    #         im.verify()
    # except:
    #     'invalid image'
    # return

    with open(out_file, 'wb') as img:
        img.write(response.content)

    body = request.form['body']
    author = request.form['author']

    # if body == '':
    #     body = 'To be or not to be'
    # if author == '':
    #     author = 'Shakespeare'
    path = meme.make_meme(out_file, body, author)
    if path.find('Enter valid image') != -1:
        return render_template('meme_form.html', bad_image=path)
    else:
        return render_template('meme.html', path=path)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/<name>/')
def index(name):
    name = escape(name)
    return render_template('page_not_found.html', name=name)


@app.route('/about/')
def about():
    return render_template('about.html')

# @app.route('/about/')
# def about_page(name):
#     return render_template('about.html', name=name)


if __name__ == "__main__":
    app.run()
