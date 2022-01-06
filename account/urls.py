from django.urls import path
from .views import user_login, user_register

urlpatterns = [
    path('log-in', user_login),
    path('register', user_register)
]