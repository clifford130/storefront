from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    return  HttpResponse("Hello, World! This is the playground app.")

def playground_home(request):
    return HttpResponse("Welcome to the playground!")