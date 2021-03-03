from django.http import HttpResponse
from django.shortcuts import render, redirect

from markets.models import Market


def all_markets(request):
    markets = Market.objects.all()
    my_ob = {
        'markets': markets
    }
    return render(request, 'markets/index.html', context=my_ob)


def index_market(request, **kwargs):
    try:
        market = Market.objects.get(pk=kwargs.get('id'))
    except Market.DoesNotExist:
        return redirect('markets:all_markets', )
    my_ob = {
        'market': market
    }
    return render(request, 'markets/a_market.html', context=my_ob)
