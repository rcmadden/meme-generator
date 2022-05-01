from abc import ABC, abstractmethod
from typing import List

from QuoteEngine import QuoteModel


class IngestInterface(ABC):
    allowed_extensions = []
 
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        pass

# An abstract method for parsing the file content (i.e., splitting each row) 
# and outputting it to a Quote object.     
    