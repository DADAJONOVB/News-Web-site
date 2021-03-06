from http.client import HTTPResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, News
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


def index(request):
    category = Category.objects.all()
    search = request.GET.get('q')
    category_name = request.GET.get('category')
    if search != '' and search is not None:
        news = News.objects.filter(title__icontains=search).filter(is_active=True)
    elif category_name != '' and category_name is not None:
        news = News.objects.filter(category__name=category_name).filter(is_active=True)
    else:
        news = News.objects.filter(is_active=True)
    context = {
        'category': category,
        'news': PagenatorPage(news, 5, request),
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


def detail(request, pk):
    category = Category.objects.all()
    new = get_object_or_404(News, id=pk)
    context = {
        'category': category,
        'new': new
    }
    return render(request, 'detail.html', context)

def create_news(request):
    if request.user.active == True:
        if request.method == 'POST':
            title = request.POST['title']
            photo = request.FILES.get('photo')
            body = request.POST['body']
            category = request.POST['category']
            new = News.objects.create(title=title, photo=photo, body=body, user=request.user)
            for cat in category:
                ct = Category.objects.get(id=cat)
                new.category.add(ct)
            return redirect('detail_url', new.id)
        else:
            return HTTPResponse('Ruxsat berilmagan')
    else:
        return HTTPResponse(False)