from django.shortcuts import render
from .models import Image,Place,Category
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):


    context = {"images":Image.get_images()}

    return render(request,"index.html",context)

