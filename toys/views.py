from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'toys/index.html',context={'welcome_text':"Welcome to Home Page"})
