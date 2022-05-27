from typing import List

from urllib3 import Retry

from .IngestInterface import IngestInterface
from QuoteEngine import QuoteModel


class TextIngestor(IngestInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        with open(path, encoding='utf-8') as file_ref:
            quotes = []
            lines = file_ref.readlines()
            for line in lines:
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('- ')
                    new_quote = QuoteModel(parse[0], (parse[1]))
                    quotes.append(new_quote)
        return quotes
