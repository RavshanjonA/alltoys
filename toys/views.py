from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Toy, User


def home(request):
    return render(request, 'toys/home.html', context={'text': 'Hello !\nWelcome to HomePage'})


def toys(request):
    toys = Toy.objects.all()
    toys = toys.filter(created_at__year=timezone.now().year)
    toys= toys.select_related('user')
    toys = toys.prefetch_related('tag')
    return render(request, 'toys/index.html', context={'toys': toys, })


def users(request):
    users = User.objects.all()

    return render(request, 'toys/member.html', context={'users': users})
