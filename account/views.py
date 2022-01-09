from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from.models import Staff, region
from main.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def PagenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')

    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list


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
    return render(request, 'dashboard/admin-dashboard.html', context)



def active_users_list(request):
    return render(request, 'dashboard/active-users-list.html', {'user':PagenatorPage(Staff.objects.filter(active=True), 10, request)})

def disactive_users_list(request):
    return render(request, 'dashboard/disactive-users-list.html', {'user':PagenatorPage(Staff.objects.filter(active=False), 10, request)})

def active_news(request):
    return render(request, 'dashboard/active-news-list.html', {'news':PagenatorPage(News.objects.filter(is_active=True), 10, request)})

def disactive_news(request):
    return render(request, 'dashboard/disactive-news-list.html', {'news':PagenatorPage(News.objects.filter(is_active=False), 10, request)})


def delete_news(request):
    try:
        new = request.GET.get('new_id')
        delete_order = News.objects.get(id=new)
        delete_order.delete()
        return redirect('dashboard_url')
    except:
        return HttpResponse(False)

def change_news(request, pk):
    new = News.objects.get(id=pk)
    active = request.POST.get('active')
    if active == 'on':
        new.is_active = True
    else:
        new.is_active = False
    new.save()
    return redirect('dashboard_url')