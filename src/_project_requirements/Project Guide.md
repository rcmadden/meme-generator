## Project Workspace: Motivational Meme Generator


```python
### Starter Code
Review the starter code: 

* Locate the sample quotes and images of Xander the pup in `src/_data/`.
* There's a basic flask server that will consume your modules and make them usable through a web interface. Check out the main code for this flask service in `app.py`.
* Check out the HTML template files in `templates/`.

To start the flask server in this workspace, run:
```sh
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload
```
> **Note:** the host and port are required to access the server from within this notebook.

Use the Open Preview button to view the output of the flask server:
```

<button id="ulab-button-d19ad458" class="ulab-btn--primary"></button>

### Quote Engine

The responsibility of this module is to load and parse quotes from files. Here's what you'll need to do to complete it:

* Create a Python module (including `__init__.py`) in a directory called `QuoteEngine`.
* Example quotes are provided in a variety of files. Take a moment to review the file formats in `./_data/SimpleLines` and `./_data/DogQuotes`.
* Implement a simple `QuoteModel` class to encapsulate the body and author.
* Implement an abstract base class, `IngestorInterface`. This class should define two methods with the following class method signatures:  `def can_ingest(cls, path) -> boolean` and  `def parse(cls, path: str) -> List[QuoteModel] `
* Implement separate strategy objects that realize the `IngestorInterface` for each file type (csv, docx, pdf, txt).
* Implement a final `Ingestor` class that realizes the `IngestorInterface` abstract base class and encapsulates your helper classes. It should implement logic to select the appropriate helper for a given file, based on filetype.

If you like, you can check your work against the `Quote Engine Module` section of the [rubric](https://review.udacity.com/#!/rubrics/2709/view).

#### Other Requirements
* All Quote classes should have clear, concise and PEP compliant docstrings.
* All code should be PEP-8 compliant.
* Common exceptions should be handled with `try-catch` blocks

### Meme Engine Module 
The Meme Engine Module is responsible for manipulating and drawing text onto images. 

The class must implement code for:
* Loading an image using Pillow (PIL).
* Resizing the image so the width is at most 500px and the height is scaled proportionally.
* Adding a quote body and a quote author to the image.
* Saving the manipulated image.
* The class must implement this instance method signature, which returns the path to the manipulated image: `make_meme(self, img_path, text, author, width=500) -> str`

You can check your work against the `Meme Generator Module` section of the [rubric](https://review.udacity.com/#!/rubrics/2709/view).

#### Other Requirements
* All Meme Generator classes have clear, concise, and PEP compliant docstrings.
* All code is PEP-8 Compliant.
* Common exceptions should be handled using `try-catch` blocks.

### Complete the README

Your README should document your code by describing your project's functionality and how to use it.

Locate the `README.md` file in the project root directory then update the README to include: 
* An overview of the project
* Instructions for setting up and running the program
* A brief description of the roles-and-responsibilities of all sub-modules including dependencies and examples of how to use the module

### Package your Application

Package the project as a command line tool and as a simple web service.

#### Create a Command-Line Interface tool

The project contains a simple cli app starter code in `meme.py`. This file contains `@TODO` tasks for you to complete. The utility can be which can be run from the terminal by invoking `python3 meme.py`

The script must take three *optional* CLI arguments:

* `--body` a string quote body
* `--author` a string quote author
* `--path` an image path

The script returns a path to a generated image.
If any argument is not defined, a random selection is used.

#### Complete the Flask app

The project contains a flask app starter code in `app.py`. This file contains `@TODO` tasks for you to complete. 

* The app uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image.
* It uses the `requests` package to fetch an image from a user submitted URL.
* The flask server must run with no errors

Complete the following tasks:
* Open the `meme.py` command line starter code and complete the `@TODOs`.

* Open the `app.py` flask web server starter code and complete the `@TODOs`. You can start the server by calling `python3 app.py` from a terminal window. 

* Check your work against the `Package your Application` section of the  [rubric](https://review.udacity.com/#!/rubrics/2709/view).

* Create a `requirements.txt` file in the project root including all project dependencies.


## Submitting Your Project

Before you submit your project, take a moment to ensure that it is ready for review:

* You have reviewed each item in the [rubric](https://review.udacity.com/#!/rubrics/2709/view) and verified you have completed it successfully.

* The requirements.txt file contains all required dependencies. 

### Submit the project

Submit your project by clicking the SUBMIT PROJECT button in the bottom right of the workspace
