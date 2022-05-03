'''The Quote Engine module is responsible for ingesting many types of files that contain quotes. 
For our purposes, a quote contains a body and an author.

This module will be composed of many classes and will demonstrate your understanding of complex inheritance, 
abstract classes, classmethods, strategy objects and other fundamental programming principles. 

The class overrides the correct methods to instantiate the class and print the model contents as: 
”body text” - author

TODO: Implement a simple QuoteModel class to encapsulat the body and the author
'''
from IngestEngine import CSVIngestor

class QuoteModel():
    def __init__(self, body, author):
        """Create a new quote."""
        self.body = body
        self.author = author
    
    def model_content(self):
        #TODO: check for quotes then add
        return f'{self.body} -{self.author}'

    def __repr__(self):
        return f'<{self.body}, -{self.author}>'
