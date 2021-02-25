from django.http import HttpResponse
from django.shortcuts import render

from .models import Toy, User


def home(request):

    return render(request, 'toys/home.html', context={'text': 'Hello !\nWelcome to HomePage'})


def toys(request):
    toys = Toy.objects.all()

    return render(request, 'toys/index.html', context={'toys': toys})


def users(request):
    users = User.objects.all()

    return render(request, 'toys/member.html', context={'users': users})
