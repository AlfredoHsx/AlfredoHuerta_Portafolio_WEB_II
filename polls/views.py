from django.shortcuts import render
from django.http import HttpResponse
from django.urls import include, path



# Create your views here.
def  index(request):
    return HttpResponse ("Hello, world. Youre at the polls index.")