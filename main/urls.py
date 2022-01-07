from django.urls import path
from .views import index, songi_yanglik, detail

urlpatterns = [
    path('', index, name='index_url'),
    path('songi', songi_yanglik, name='songi_url'),
    path('detail/<int:pk>/', detail)
]