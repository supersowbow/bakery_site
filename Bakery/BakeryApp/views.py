from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is the index page.")

def gallery(request):
    return HttpResponse("This is the gallery page.")
def gallery_wedding(request):
    return HttpResponse("This the wedding cake page from the gallery page.")

def about(request):
    return HttpResponse("This is the about page.")

def catering(request):
    return HttpResponse("This is the catering page.")

def order(request):
    return HttpResponse("This is the order page.")

def contact(request):
    return HttpResponse("This is the contact page.")
