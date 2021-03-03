from django.urls import path, include

from markets import views
from markets.views import ProductView

app_name = 'markets'
urlpatterns = [
    path('show/', views.all_markets, name='all_markets'),
    path('show/<int:id>', views.index_market, name='index_markets'),
    path('template/', ProductView.as_view(), name='template')
]
