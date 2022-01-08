from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from.models import Staff, region
from main.models import *


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def user_register(request):
    return render(request, 'account/register.html')

def dashboard(request):
    if request.user.is_staff == True:
        active_user = Staff.objects.filter(active=True).count()
        disactive_user = Staff.objects.filter(active=False).count()
        active_news = News.objects.filter(is_active=True).count()
        disactive_news = News.objects.filter(is_active=False).count()
        context ={
            'active_user':active_user,
            'disactive_user':disactive_user,
            'active_news':active_news,
            'disactive_news':disactive_news
        }
        return render(request, 'account/admin-dashboard.html', context)