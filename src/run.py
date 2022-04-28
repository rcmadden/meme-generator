from IngestEngine import DocxIngestor, CSVIngestor

path_prefix = '/Users/russiam/_Dev/udacity-meme-generator/meme-generator/src'
quote_files = [path_prefix + '/_data/DogQuotes/DogQuotesCSV.csv']


print(CSVIngestor.parse(quote_files[0]))