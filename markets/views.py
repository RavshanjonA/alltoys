from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from markets.models import Market, Product


class ProductView(TemplateView):
    template_name = 'markets/template.html'
    extra_context = {'source': 'Product Page'}


class ProductListView(ListView):
    model = Product
    template_name = 'product/index.html'

    def get_queryset(self):
        product = Product.objects.all()
        product.order_by('-name')
        return product


class ProductItemView(DetailView):
    model = Product
    template_name = 'product/item.html'


class ProductDeleteView(DetailView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('markets:product ')


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'descirption']
    template_name = 'product/create.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'descirption']
    template_name = 'product/update.html'


def all_markets(request):
    markets = Market.objects.all().order_by('id')
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
