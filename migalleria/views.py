from django.shortcuts import render
from .models import Image,Place,Category
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):
    images = Image.get_images()


    three_images_list = [images[x:x+3] for x in range(0, len(images),3)]


    context = {"images":images}

    return render(request,"index.html",context) 
