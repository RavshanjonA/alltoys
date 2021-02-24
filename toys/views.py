from django.http import HttpResponse
from django.shortcuts import render

from .models import Toy, User


def home(request):
    toys = Toy.objects.all()
    users = User.objects.all()

    return render(request, 'toys/index.html', context={'users': users, 'toys': toys})
