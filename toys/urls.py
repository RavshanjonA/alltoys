from django.urls import path
from .views import home, toys, users, get_detail

app_name = 'toys'
urlpatterns = [
    path('', home, name='home'),
    path('toys/', toys, name='toys'),
    path('toys/<int:id>', get_detail, name='get_detail'),
    path('users/', users, name='users'),

]
