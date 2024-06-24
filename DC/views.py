from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def panth(request):
    return HttpResponse("<h1> Rishabh panth is the captain as well as wicket-keeper")

