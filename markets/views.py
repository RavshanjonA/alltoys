from django.http import HttpResponse
from django.shortcuts import render

from markets.models import Market


def index(request):
    return HttpResponse("<h1> Hello this is Market place</h1>")


def all_markets(request):
    markets = Market.objects.all()
    my_ob = {
        'markets': markets
    }
    return render(request, 'markets/index.html', context=my_ob)


def index_market(request, **kwargs):
    market = Market.objects.get(pk=kwargs.get('id'))
    my_ob = {
        'market': market
    }
    return render(request, 'markets/a_market.html', context=my_ob)
