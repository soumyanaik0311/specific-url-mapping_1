from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rohit(request):
    return HttpResponse("<h1> Rohit Sharma is a great player </h1>")

def bumrah(request):
    return HttpResponse("<h1> bumrah is a great bowler </h1>")