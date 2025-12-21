from whoosh.fields import Schema, TEXT
from whoosh.scoring import TF_IDF
schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True))
import os
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
from whoosh.index import create_in
ix = create_in("indexdir", schema)
writer = ix.writer()
writer.add_document(
    title="The Stars Beyond Us",
    content="We’ve always looked up. Before we built cities, before we named constellations, before we understood what light-years meant, we looked up and wondered. The stars were gods, maps, omens. They were stories passed down around fires, stitched into mythologies, guiding sailors across oceans and lovers across lifetimes.\n\nBut now, in the age of algorithms and artificial suns, we forget to look. We forget that above the hum of traffic and the glow of screens, there’s a canvas that’s been painted for billions of years. The stars beyond us aren’t just distant balls of gas. They’re reminders. Of how small we are. Of how beautiful smallness can be.\n\nThere's a kind of humility in stargazing. You realize that your heartbreak, your triumph, your confusion—they’re all part of a fleeting moment in a universe that doesn’t flinch. And yet, somehow, that doesn’t make them meaningless. It makes them precious. Because in all this vastness, you get to feel. You get to wonder.\n\nI remember lying on a rooftop once, years ago, wrapped in a blanket and silence. The stars were sharp that night, like they’d been waiting for someone to notice. I didn’t know their names. I didn’t need to. They were there. And I was there. And that was enough.\n\nWe chase stars now with telescopes and rovers, with equations and ambition. We send metal hearts into orbit, hoping they’ll whisper back secrets. And they do. But the real magic isn’t just in the data. It’s in the awe. The kind that makes you pause mid-sentence, mid-scroll, mid-life—and look up.\n\nSo tonight, if you can, step outside. Find a patch of sky. Let the stars remind you that you’re part of a story older than language. That you’re made of the same dust. That beyond the noise and the news and the next thing, there’s a quiet brilliance waiting to be seen.\n\nThe stars beyond us are not unreachable. They are reflections of the wonder within us."
)
writer.add_document(
    title="What Is Literature?",
)
writer.commit()
from whoosh.qparser import QueryParser
def search(query_string):
    with ix.searcher(weighting=TF_IDF) as searcher:
        query = QueryParser("content", ix.schema).parse(query_string)
        results = searcher.search(query)
        return [(r["title"], r["content"]) for r in results]

if __name__ == "__main__":
    while True:
        user_query = input("Enter your search query (or type 'quit' to exit): ").strip()
        if user_query.lower() == 'quit':
            break
        if user_query:
            results = search(user_query)
            if results:
                for i, (title, content) in enumerate(results, start=1):
                    print(f"Result {i}:")
                    print(f"  Title: {title}")
                    print(f"  Content: {content}")
            else:
                print("No results found.")
        else:
            print("Please enter a valid query.")