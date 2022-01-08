from os import name
from django.urls import path
from .views import index, songi_yanglik, detail, create_news

urlpatterns = [
    path('', index, name='index_url'),
    path('songi', songi_yanglik, name='songi_url'),
    path('detail/<int:pk>/', detail, name='detail_url'),
    path('create-news', create_news, name='create_news_url')
]