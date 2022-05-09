from abc import ABC, abstractmethod
from typing import List

from QuoteEngine import QuoteModel


class IngestInterface(ABC):
    """An abstract method for parsing the file type and outputting it to a Quote object."""     
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Separate strategy objects realize IngestorInterface for each file type (csv, docx, pdf, txt)."""
        pass
