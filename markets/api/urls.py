from django.urls import path, include

from markets import views
from markets.views import ProductView, ProductListView, ProductItemView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'markets'
urlpatterns = [
    path('show/', views.all_markets, name='all_markets'),
    path('show/<int:id>', views.index_market, name='index_markets'),
    path('template/', ProductView.as_view(), name='template'),
    path('product/', ProductListView.as_view(), name='product'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>', ProductItemView.as_view(), name='product_item'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]
