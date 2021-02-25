from django.urls import path
from .views import home, toys, users


urlpatterns = [
    path('', home, name='home'),
    path('toys/', toys, name='toys'),
    path('users/', users, name='users'),

]
