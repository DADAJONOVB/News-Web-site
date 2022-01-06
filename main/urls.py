from django.urls import path
from .views import index, songi_yanglik, yanglik_qoshish

urlpatterns = [
    path('', index),
    path('songi', songi_yanglik),
    path('add', yanglik_qoshish)
]