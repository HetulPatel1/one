from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def page1(request):
    return HttpResponse('<marquee><h1>Welcome to firstpage</h1></marquee>')

def page2(request):
    return HttpResponse('<b>Welcome to gallery</b>')