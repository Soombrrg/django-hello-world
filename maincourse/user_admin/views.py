from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse("<html><h1>Hello World</h1></html>")

def about(request):
    return HttpResponse("<html><h1>about</h1></html>")