from django.urls import path
from .views import (
    user_login, 
    user_register, 
    dashboard, 
    disactive_news, 
    delete_news, 
    change_news, 
    active_news,
    active_users_list,
    disactive_users_list,
    change_user_status,
    add_category,
    user_logout
    )

urlpatterns = [
    path('log-in/', user_login, name='login_url'),
    path('register/', user_register, name='register_url'),
    path('log-out/', user_logout, name='logout_url'),
    #dashboard
    path('dashboard/', dashboard, name='dashboard_url'),
    # tables
    path('disactive-news/', disactive_news, name='disactive_news_url'),
    path('active-news/', active_news, name='active_news_url'),
    path('active-users/', active_users_list, name='active_users_list_url'),
    path('disactive-users/', disactive_users_list, name='disactive_users_list_url'),
    # change delete
    path('delete-news/', delete_news, name='delete_news_url'),
    path('change-news/<int:pk>/', change_news, name='change_news_url'),
    path('change-user-status/<int:pk>/', change_user_status, name='change_user_status_url'),
    path('add-category/', add_category, name='add_category_url')
]