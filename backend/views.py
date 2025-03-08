from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World! This is a response without an HTML template.")

def thanveer(request):
    return HttpResponse("Learning How to do templates Http Response and Html response.")


