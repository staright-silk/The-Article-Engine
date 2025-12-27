from whoosh.fields import Schema, TEXT
from whoosh.scoring import TF_IDF
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_DIR = os.path.join(BASE_DIR, "indexdir")

schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True))

if not os.path.exists(INDEX_DIR):
    os.mkdir(INDEX_DIR)
    ix = create_in(INDEX_DIR, schema)
    writer = ix.writer()

    writer.add_document(
        title="The Stars Beyond Us",
        content="We’ve always looked up..."
    )

    writer.add_document(
        title="What Is Literature?",
        content="Literature is the expression of human thought..."
    )

    writer.commit()
else:
    ix = open_dir(INDEX_DIR)

def search_articles(query_string):
    with ix.searcher(weighting=TF_IDF()) as searcher:
        query = QueryParser("content", ix.schema).parse(query_string)
        results = searcher.search(query)
        return [{"title": r["title"], "content": r["content"]} for r in results]
