'''The Quote Engine module is responsible for ingesting many types of files that contain quotes. 
For our purposes, a quote contains a body and an author.

This module will be composed of many classes and will demonstrate your understanding of complex inheritance, 
abstract classes, classmethods, strategy objects and other fundamental programming principles. 

The class overrides the correct methods to instantiate the class and print the model contents as: 
”body text” - author

TODO: Implement a simple QuoteModel class to encapsulat the body and the author
'''

class QuoteModel():
    def __init__(self, body_text, author):
        """Create a new quote."""
        self.body_text = body_text
        self.author = author
    
    def model_content(self):
        return f'{self.body_text} -{self.author}'

    def __repr__(self):
        return f'{self.body_text} -{self.author}'


if __name__ == "__main__":
     quote_1 = QuoteModel("To bork or not to bork", "Bork")
     quote_2 = QuoteModel("He who smelt it...", "Stinky") 
     print(quote_1.model_content)
     print(quote_2)