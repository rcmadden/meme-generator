from PIL import Image, ImageFont, ImageDraw
'''MemeGenerator module with the following responsibilities:

Loading of a file from disk

'''
class MemeEngine():
    def __init__(self, out_dir):
        """
        Arguments:
            out_dir {str} -- for where to save the generated images.
        Returns:
            str -- the file path the output images.
        """
        self.out_dir = out_dir
        print(self.out_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme by adding a caption to an image (string input) 
        with a body and author to a random location on the image.

        Transform image by resizing to a maximum width 
        of 500px while maintaining the input aspect ratio

        The class depends on the Pillow library to 
        complete the defined, incomplete method signatures so 
        that they work with JPEG/PNG files.
        """
        self.img_path = img_path
        self.text = text
        self.author = author
        self.width = width

        meme_body = self.text + self.author
        out_file = 'out.' + self.img_path.split('.')[-1]
        # out_file = self.img_path.split('.')[-1]


        img = Image.open(img_path)
        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)
    # NEAREST is deprecated and will be removed in Pillow 10 (2023-07-01). Use Resampling.NEAREST or Dither.NONE instead.
        if meme_body is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./_fonts/LilitaOne-Regular.ttf', size=25)
            draw.text((10, 30), meme_body, font=font, fill='white')
        
        # img.save(self.out_dir + out_file)
        img.save(self.out_dir + out_file)
        return self.out_dir + out_file

        #  return out_path of generated meme?  
        # return img_path, text, author
