from typing import List
import subprocess
import os
import random

from .IngestInterface import IngestInterface
from .QuoteEngine import QuoteModel

class PDFImporter(IngestInterface):
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        
        file_ref = open(tmp, "r")
        quotes = []
        
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(',')
                new_quote = QuoteModel(parse[0], int(parse[1]), bool(parse[2]))
                quotes.append(new_cat)
                
        file_ref.close()
        os.remove(tmp)
        return quotes