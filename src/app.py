import os
import random
import requests
from flask import Flask, render_template, request
from markupsafe import escape
from IngestEngine import Ingestor
from MemeGenerator import MemeEngine


app = Flask(__name__)
# ELABORATE: the following line required for hosting provider. Unable to set on host, but withoug it thows OSError.
# looking for a way to set it so I do not have to comment and uncomment each time I push and pull code to git/web host.
# os.chdir('/home/russiam/meme-generator/src') # set pythonanywhere cwd
meme = MemeEngine('./static/tmp')


def setup():
    """ Load all resources """
    # ELABORATE: Possible Feature - toggle between dog Meme Generator and my custom Quote generator.
    # Andy directior on how to implement such a feature?
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

    try:
        os.remove(out_path + 'jpg')
    except:
        print('no jpg file exists:')

    try:
        os.remove(out_path + 'png')
    except:
        print('no png file to remove')

    img_url = request.form['image_url']
    image_type = img_url.split('.')[-1]
    if image_type == 'jpg' or image_type == 'png':
        out_file = out_path + image_type
        response = requests.get(img_url)
    else:
        bad_image = 'url must end with .png or .jpg'
        return render_template('meme_form.html', bad_image=bad_image)
    # ELABORATE: is there a way to check the file before saving?
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
    
    # prints default text if none entered in Creator
    # only works sometimes
    if body == '':
        body = 'To be or not to be'
    if author == '':
        author = 'Shakespeare'

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


if __name__ == "__main__":
    app.run()
