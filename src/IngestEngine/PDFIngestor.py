from typing import List
import subprocess
import os
import random

from .IngestInterface import IngestInterface
from QuoteEngine import QuoteModel


class PDFIngestor(IngestInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'/tmp/{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', '-layout', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            # print('outside: ', line, type(line), line=='fi')
            # if (len(line) > 1 and line != 'fi') or line != 'fi fi fi':
            if len(line) > 1:
                if line != 'fi' and line != 'fi fi fi':
                    parse = line.split(' - ')
                    # print('inside: ', line, 'parse', parse)
                    new_quote = QuoteModel(parse[0], (parse[1]))
                    quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
