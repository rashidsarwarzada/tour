from django.shortcuts import render 
from django.http import HttpResponse


def calcuate():
    x = 1
    y = 2
    return x


def say_hello(request):
    x = calcuate()
    return render(request, 'hello.html', {'name': 'mosh'})



