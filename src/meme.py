import argparse
from email import parser
import os
import random
from IngestEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeGenerator import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an optional path, body or quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path        

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
        print(quote)

    elif len(body) > 40:
        raise Exception('Qutoe Body should be less than 40 characters')
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')

    meme = MemeEngine('./tmp')
    result = meme.make_meme(img, body, author)

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, help='path to an image file')
    parser.add_argument('-b', '--body', type=str, help='quote body to add to the image')
    parser.add_argument('-a', '--author' ,type=str, help='quote author to add to the image')

    args = parser.parse_args()
    generate_meme(args.path, args.body, args.author)
