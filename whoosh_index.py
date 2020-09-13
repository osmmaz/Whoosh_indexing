import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import sys


def createSearchableData(root):
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT, textdata=TEXT(stored=True))
    in_path="./indexdir" # Insert here where you want you save the Index
    if not os.path.exists(in_path): 
        os.mkdir(in_path)

    # Creating an index writer to add document as per schema
    ix = create_in(in_path, schema)
    writer = ix.writer()

    filepaths = [os.path.join(root, i) for i in os.listdir(root)]
    for path in filepaths:
        fp = open(path)
        print(path)
        text = fp.read()
        
        writer.add_document(title=path.split("/")[6], path=path,  content=text, textdata=text)
        
        fp.close()
    writer.commit()


root = "./Base" # Insert here the path of your base if you want to change it
createSearchableData(root)
