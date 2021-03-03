from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Toy, User


def home(request):
    return render(request, 'toys/home.html', context={'text': 'Hello !\nWelcome to HomePage'})


def get_detail(request, **kwargs):
    try:
        toy = Toy.objects.get(pk=kwargs.get('id'))

    except Toy.DoesNotExist:
        return redirect('toys:toys', )
    my_object = {
        'toy': toy
    }
    return render(request, 'toys/get_detail.html', context=my_object)


def toys(request):
    toys = Toy.objects.all()
    toys = toys.filter(created_at__year=timezone.now().year)
    toys = toys.select_related('user')
    toys = toys.prefetch_related('tags')
    return render(request, 'toys/index.html', context={'toys': toys, })


def users(request):
    users = User.objects.all()

    return render(request, 'toys/member.html', context={'users': users})
