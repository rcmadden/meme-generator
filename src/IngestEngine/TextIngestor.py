from typing import List

from .IngestInterface import IngestInterface
from QuoteEngine import QuoteModel

from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor

class Importer(IngestInterface):
    ingestors = [DocxIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)