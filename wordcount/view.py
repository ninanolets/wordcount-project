from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")

def wordcount(request):
    fulltext = request.GET["fulltext"]
    wordslist = fulltext.lower().split()

    my_dict = {k: wordslist.count(k) for k in wordslist}
    key = sorted(my_dict.items(), key=lambda value: value[-1], reverse=True) # sort by last element

    return render(request, "count.html", { 
        "fulltext": fulltext, 
        "count": len(wordslist), 
        "highestcount": key[0][-1],
        "highestword": key[0][0],
        "items": key
    })

def aboutme(request):
    return render(request, "aboutme.html")
