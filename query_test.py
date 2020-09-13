from whoosh import qparser
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
ix = open_dir("./indexdir") # Set here the path of the index created by Whoosh
query_str="petrole fule" # Set here the Query
# Top 'n' documents as result
topN = 100 # The size of the result

with ix.searcher(weighting=scoring.TF_IDF) as searcher:
    query=QueryParser("content", ix.schema).parse(query_str)
    parser = qparser.QueryParser("content", schema=ix.schema,group=qparser.OrGroup) # Using an Or group for the query
    query=parser.parse(query_str)
    print(query)
    #query="(content:petrole AND content:fule)" # you can use this instead of the parser
    results = searcher.search(query, limit=topN)
    for r in results:
        print(r['title'], str(r.score))
