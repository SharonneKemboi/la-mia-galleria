
from django.shortcuts import render
from .models import Image,Place,Category
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):
    gallery = Image.get_images()


    context = {"images":gallery}

    return render(request,"index.html",context) 

def search(request):
    if "term" in request.GET and request.GET["term"]:

        term = request.GET.get("term")
        gallery = Image.search_image(term)
        if gallery != "No images found":
            message = "Gallery of " + term + ""

            return render(request, "search.html", {"images":gallery,"message":message,"title":term.capitalize()})
        else:
            message = "No images found"
            return render(request, "search.html", {"images":[],"message":message,"title":term.capitalize()})


def places_page(request):
    return render(request,"places.html",{"title":"Places"})


    