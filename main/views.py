from django.shortcuts import render
from .models import Category

def index(request):
    category = Category.objects.all()
    return render(request, 'index.html', {'category':category})


def songi_yanglik(request):
    return render(request, 'songi-yanglik.html')


def yanglik_qoshish(request):
    return render(request, 'joylash.html')


def base(request):
    return render(request, 'base.html')