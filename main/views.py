from django.shortcuts import get_object_or_404, render
from .models import Category, News

def index(request):
    category = Category.objects.all()
    news = News.objects.filter(is_active=True)[:5]
    context = {
        'category': category,
        'news': news
    }
    return render(request, 'index.html', context)


def songi_yanglik(request):
    category = Category.objects.all()
    news = News.objects.filter(is_active=True)[:5]
    context = {
        'category': category,
        'news': news
    }
    return render(request, 'songi-yanglik.html', context)


def base(request):
    category = Category.objects.all()
    return render(request, 'base.html', {'category':category})

def detail(request, pk):
    category = Category.objects.all()
    new = get_object_or_404(News, id=pk)
    context = {
        'category': category,
        'new': new
    }
    return render(request, 'detail.html', context)