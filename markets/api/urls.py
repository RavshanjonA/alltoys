from django.urls import path, include

from markets import views

app_name = 'markets'
urlpatterns = [
    path('', views.index, name='market'),


]
