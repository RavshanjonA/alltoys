from django.urls import path, include

from markets import views

app_name = 'markets'
urlpatterns = [
    path('', views.index, name='market'),
    path('show/', views.all_markets, name='all_markets'),
    path('show/<int:id>', views.index_market, name='index_markets'),

]
