"""The Quote Engine module is responsible for ingesting many
types of files that contain quotes. For our purposes, a quote
contains a body and an author.

The class overrides the correct methods to instantiate the class
and print the model contents as:
'body text' - author.
"""


class QuoteModel():
    """A simple class to encapsulate the body and the author."""

    def __init__(self, body, author):
        """Create a new quote."""
        self.body = body
        self.author = author

    def model_content(self):
        """Not used."""
        return f'{self.body} -{self.author}'

    def __repr__(self):
        """Represent new quote."""
        return f'<{self.body}, -{self.author}>'
