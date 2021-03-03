from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from markets.models import Market

class ProductView(TemplateView):
    template_name = 'markets/template.html'
    extra_context = {'source': 'Product Page'}

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
