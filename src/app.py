import os
import random
from urllib import response
import requests
from flask import Flask, render_template, abort, request

from IngestEngine import Ingestor
from MemeGenerator import MemeEngine

from markupsafe import escape 

app = Flask(__name__)
app.debug=True
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
    with open(out_file, 'wb') as img:
        img.write(response.content)

    body = request.form['body']
    author = request.form['author']
    path = meme.make_meme(out_file, body, author)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()