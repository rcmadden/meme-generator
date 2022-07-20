# meme-generator
"Meme generator" is a multimedia application to dynamically generate memes, including an image with an overlaid quote.  Inspirational quotes were substituted for memes, and images from the Isle of Skye, Scottland were selected from unsplash.com.

The application:

    Reads quotes from a variety of filetypes (PDF, Word Documents, CSVs, and Text files).
    
    Loads, manipulates, and saves images.

    Accepts dynamic user input through a command-line tool and a Flask web service.

    The random button selects a random image and a random quote. Then writes the quote text to a random location on the 'y' axis of the image.

Instructions for setting up and running the program: 
    Includes a simple cli utlity in meme.py. The utility can be run from the terminal by invoking with:

``` 
python3 meme.py
```

    The script accepts three optional CLI arguments:
        --body - a string quote body
        --author - a string quote author
        --path - an image path

    The script returns a path to a generated image. If any argument is not defined, a random selection is used.

    The project contains a flask app in index.py.  The app uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image.

    It uses the requests package to fetch an image from a user submitted URL.

Roles-and-responsibilities of sub-modules:

    A. QuoteEngine
        - Responsible for ingesting many types of files that contain quotes.
        - A quote contains a body and an author: 
            "This is a quote body" - Author
    B. IngestEngine
        Ingestors
            Separate strategy objects realize the Abstract Base Class IngestorInterface for each file type.  Ingestors utilize the following libraries:
            * CSVIngestor.py - pandas library
            * DocxIngestor.py - python-docx library
            * TextIngestor.py - the native file library
            * PDFIngestor.py - the subprocess module to call the C program pdftotext CLI utility<https://www.xpdfreader.com/pdftotext-man.html>
            To Install:
                bash - sudo apt-get install -y xpdf
                mac - brew install xpdf
                https://github.com/kermitt2/xpdf-4.00
                * follow install instructions and ensure to include path to CMAKEList.txt
            
                NOTE: Did NOT use the pdftotext PIP Library - purpose is to demonstrate use of the Python subprocess module.

        A final Ingestor class realizes the IngestorInterface Abstract Base Class and encapsulates the helper classes to select the appropriate ingestor for a given file based on filetype.
        
         IngestorInterface defines two methods with the following class method signatures:

                def can_ingest(cls, path: str) -> boolean
                def parse(cls, path: str) -> List[QuoteModel]

         
    C. MemeGenerator
        Utilizes the Pillow library to perform basic image operations

Visual Studio Code Setup Notes:
1. set cwd in launch.json file: "cwd": "/Path/To/app.py"
2. set project to use venv cmd + shift + p paste path to .venv in selection box: 
* https://code.visualstudio.com/docs/python/environments
* https://code.visualstudio.com/docs/python/tutorial-flask

3. works best if root folder in VS code explorer contains app.py
4. flask will not run if not in /src directory when flask run called


Udacity Git Style Guide: https://udacity.github.io/git-styleguide/

