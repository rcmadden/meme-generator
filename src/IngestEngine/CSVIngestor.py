from typing import List
import pandas

from .IngestInterface import IngestInterface
from QuoteEngine import QuoteModel

class CSVIngestor(IngestInterface):
    allowed_extensions = ['csv']

    # print('List[QuoteModel]', List[QuoteModel])

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        # print('List[QuoteModel]', List[QuoteModel])
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes

        # def parse(cls, path: str) -> List[QuoteModel]: #START: DEGUG this datatype
