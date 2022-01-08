from django.urls import path
from .views import user_login, user_register, dashboard

urlpatterns = [
    path('log-in', user_login, name='login_url'),
    path('register', user_register, name='register_url'),
    path('log-out', user_register, name='logout_url'),
    path('dashboard', dashboard, name='dashboard')
]