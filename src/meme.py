import argparse
from email import parser
import os
import random
from IngestEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeGenerator import MemeEngine

# @TODO [x]Import your Ingestor and MemeEngine classes


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        # for root, dirs, files in os.walk(images):
        for root, dirs, files in os.walk('./_data/photos/dog/'):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, help='path to an image file')
    parser.add_argument('-b', '--body', type=str, help='quote body to add to the image')
    parser.add_argument('-a', '--author' ,type=str, help='quote author to add to the image')

    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
