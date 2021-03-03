from django.contrib import admin

from markets.models import Market, Product

admin.site.register(Product)
admin.site.register(Market)