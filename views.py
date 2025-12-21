from django.shortcuts import render
from .whoosh_engine import search_articles

def search_view(request):
    query= request.GET.get("q","")
    results=[]

    if query:
        results=search_articles(query)
    return render (request, "search.html",{
        "query": query,
        "results": results
    } )   