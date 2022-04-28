from abc import ABC, abstractmethod

class IngestInterface(ABC):
    allowed_extensions = []
 
    @classmethod
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path):
        pass

# An abstract method for parsing the file content (i.e., splitting each row) 
# and outputting it to a Quote object.     
    