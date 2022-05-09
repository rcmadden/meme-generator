# meme-generator
"Meme generator" is a multimedia application to dynamically generate memes, including an image with an overlaid quote.

The application:

    Reads quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
    
    Loads, manipulates, and saves images.

    Accepts dynamic user input through a command-line tool and a Flask web service.

Instructions for setting up and running the program: 
    Includes a simple cli utlity in meme.py. The utility can be run from the terminal by invoking python3 meme.py

    The script may take three optional CLI arguments:
        --body a string quote body
        --author a string quote author
        --path an image path

    The script returns a path to a generated image. If any argument is not defined, a random selection is used.

    The project contains a flask app in app.py.  The app uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image.

    It uses the requests package to fetch an image from a user submitted URL.

Roles-and-responsibilities of sub-modules: 
    QuoteEngine
        Responsible for ingeting many types of files that contain quotes.
        A quote contains a body and an author: 
            "This is a quote body" - Author
    IngestEngine
        Ingestors
            An abstract base class, IngestorInterface defines two methods with the following class method signatures:

                def can_ingest(cls, path: str) -> boolean
                def parse(cls, path: str) -> List[QuoteModel]

        Separate strategy objects realize IngestorInterface for each file type (csv, docx, pdf, txt).
        
        A final Ingestor class realizes the IngestorInterface abstract base class and encapsulates the helper classes to select the appropriate ingestor for a given file based on filetype utilizing the following libraries:
            CSVIngestor.py - pandas library
            DocxIngestor.py - python-docx library
            TextIngestor.py - the native file library
            PDFIngestor.py - the subprocess module to call the C program pdftotext CLI utility<https://www.xpdfreader.com/pdftotext-man.html>
            
            NOTE: Did NOT use the pdftotext PIP Library - purpose is to demonstrate use of the subprocess module.

    MemeGenerator
        Utilizes the Pillow library to perform basic image operations

Visual Studio Code Notes:
1. set cwd in launch.json file: "cwd": "/Path/To/app.py"
2. set project to use venv cmd + shift + p paste path to .venv in selection box: https://code.visualstudio.com/docs/python/environments

https://code.visualstudio.com/docs/python/tutorial-flask
3. works best if root folder in vs code explorer contains app.py
