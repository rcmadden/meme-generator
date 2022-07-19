"""MemeGenerator module creates meme.

Loads a file from disk.
Transforms image by resizing to a maximum width of 500px while maintaining the
input aspect ratio.
Adds a caption to an image (string input) with a body and author to a random
location on the image.
"""

from PIL import Image, ImageFont, ImageDraw, UnidentifiedImageError
import random
import textwrap
import os


class MemeEngine():
    """
    Argument: out_dir {str} -- for where to save the generated images.

    Returns: str -- the file path the output image.
    """

    def __init__(self, out_dir):
        self.out_dir = out_dir

    def make_meme(self, img_path, text, author, width=500, bad_image=None) -> str:
        """Create meme object."""
        self.img_path = img_path
        self.text = text
        self.author = author
        self.width = width
        self.bad_image = bad_image
        meme_body = f'{self.text} -{self.author}'
        watermark = 'QuoteSkye.com'
        # meme_body = QuoteModel.model_content(self.text, self.author) #TypeError: QuoteModel.model_content() takes 1 positional argument but 2 were given
        out_file = '.' + self.img_path.split('.')[-1]

        # ELABORATE Cathes PIL Error, but attempted to prevent bad image from being saved, which would be preferred?
        # source: https://stackoverflow.com/questions/63656089/how-to-catch-pil-unidentifiedimageerror-in-except
        try:
            img = Image.open(img_path)
        except UnidentifiedImageError:
            try:
                os.remove(img_path)
                bad_image = 'Could not open image file. Enter valid image url.'
                return bad_image

            except:
                print(f'memeEng no img exits: {img_path}')
            return

        randomYAxis = random.randrange(30, 225, 50)

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.Resampling.NEAREST)
            
        if meme_body is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./_fonts/LilitaOne-Regular.ttf', size=25)
            watermarkFont = ImageFont.truetype('./_fonts/LilitaOne-Regular.ttf', size=15)
            waterMarkWidth = font.getlength(watermark)
            margin = 40

            for line in textwrap.wrap(meme_body, width=40):
                draw.text((margin, randomYAxis), line, font=font, fill='white')
                randomYAxis += font.getsize(line)[1]

            draw.text((((img.width + (margin))-(waterMarkWidth)), img.height-10), watermark, fill="white", anchor="ls", font=watermarkFont)
 
        try:
            img.save(self.out_dir + out_file)
        except ValueError as err:
            print('Reason: ', err)

        return self.out_dir + out_file
