from django.urls import path
from .views import user_login, user_register, dashboard, disactive_news, delete_news, change_news, active_news

urlpatterns = [
    path('log-in', user_login, name='login_url'),
    path('register', user_register, name='register_url'),
    path('log-out', user_register, name='logout_url'),
    path('dashboard', dashboard, name='dashboard_url'),
    path('disactive-news', disactive_news, name='disactive_news_url'),
    path('active-news', active_news, name='active_news_url'),
    path('delete-news', delete_news, name='delete_news_url'),
    path('change-news/<int:pk>/', change_news, name='change_news_url')
]