from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello World")

def home(request):
    return HttpResponse("<h1>welcome to home page<h1>")    

def html_demo1(request):
    return render(request,"first.html")    

def bhavya(request):
    return render(request,"bhavya\second.html")