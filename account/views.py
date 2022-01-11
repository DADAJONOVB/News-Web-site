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
        print(form)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard_url')
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
        users = Staff.objects.filter(active=True)[:3]
        regions = region.objects.all()
        category = Category.objects.all()
        number = []
        object = []
        for n in region.objects.all():
            number.append(n.staff.count())
            object.append(n.name)
        context ={
            'active_user':active_user,
            'disactive_user':disactive_user,
            'active_news':active_news,
            'disactive_news':disactive_news,
            'users':users,
            'regions':regions,
            'number': number,
            'object': object,
            'category':category 
        }
        return render(request, 'dashboard/admin-dashboard.html', context)
    elif request.user.is_staff == False:
        user = request.user
        news = News.objects.filter(user=user)
        colegiya = Staff.objects.filter(region=request.user.region)[:3]
        category = Category.objects.all()
        context = {
            'user':user,
            'colegiya':colegiya,
            'news':PagenatorPage(news, 5, request),
            'category':category 
        }
        return render(request, 'dashboard/dashboard.html', context)
            


def active_users_list(request):
    user = Staff.objects.filter(active=True)
    category = Category.objects.all()
    context = {
        'user' : PagenatorPage(user, 10, request),
        'category': category
    }
    

    return render(request, 'dashboard/active-users-list.html', context)

def disactive_users_list(request):
    category = Category.objects.all()
    user = Staff.objects.filter(active=False)
    context = {
        'user':PagenatorPage(user, 10, request),
        'category': category
    }
    return render(request, 'dashboard/disactive-users-list.html', context)

def active_news(request):
    category = Category.objects.all()
    news = News.objects.filter(is_active=True)
    context = {
        'news':news,
        'category':category
    }
    return render(request, 'dashboard/active-news-list.html', context)

def disactive_news(request):
    category = Category.objects.all()
    news = News.objects.filter(is_active=False)
    context = {
        'news':news,
        'category':category
    }
    return render(request, 'dashboard/disactive-news-list.html', context)


def delete_news(request):
    try:
        new = request.GET.get('new_id')
        delete_order = News.objects.get(id=new)
        delete_order.delete()
        return redirect('dashboard_url')
    except:
        return HttpResponse(False)

def change_news(request, pk):
    new = get_object_or_404(News, id=pk)
    active = request.POST.get('active')
    if active == 'on':
        new.is_active = True
    else:
        new.is_active = False
    new.save()
    return redirect('dashboard_url')

def change_user_status(request, pk):
    user = get_object_or_404(Staff, id=pk)
    active = request.POST.get('active')
    if active == 'on':
        user.active =True
    else:
        user.active = False
    user.save()
    return redirect('dashboard_url')