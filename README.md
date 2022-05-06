# meme-generator
"meme generator" is a multimedia application to dynamically generate memes, including an image with an overlaid quote.

The application:

    Reads quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
    
    Loads, manipulates, and save images.

    Accepts dynamic user input through a command-line tool and a web service. 

instructions for setting up and running the program: 
    a simple cli utlity in meme.py. The utility can be run from the terminal by invoking python3 meme.py

    The script must take three optional CLI arguments:

        --body a string quote body
        --author a string quote author
        --path an image path

    The script returns a path to a generated image. If any argument is not defined, a random selection is used.

    The project contains a flast app in app.py.  The app uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image.

    It uses the requests package to fetch an image from a user submitted URL.

a brief description of the roles-and-responsibilities of all sub-modules including dependencies and examples of how to use the module:

The PDFIngestor class utilizes the subprocess module to call the C program pdftotext CLI utility—creating a pipeline that converts PDFs to text <https://www.xpdfreader.com/pdftotext-man.html> and then ingests the text.

NOTE: Do not use the pdftotext PIP Library - purpose is to demonstrate use of the subprocess module.

Visual Studio Code Notes:
1. set cwd in launch.json file: "cwd": "/Path/To/app.py"
2. set project to use venv cmd + shift + p paste path to .venv in selection box: https://code.visualstudio.com/docs/python/environments
