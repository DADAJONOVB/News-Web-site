from django.shortcuts import get_object_or_404, render
from .models import Category, News

def index(request):
    category = Category.objects.all()
    news = News.objects.filter(is_active=True)
    search = request.GET.get('q')
    category = request.GET.get('category')
    if search is not None:
        news = News.objects.filter(title__icontains=search)
    elif category is not None:
        news =  News.objects.filter(category__name=category)
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
    if request.method == 'POST':
        print(True)
    else:
        category = Category.objects.all()
        new = get_object_or_404(News, id=pk)
        context = {
            'category': category,
            'new': new
        }
    return render(request, 'detail.html', context)

def create_news(request):
    if request.method == 'POST':
        title = request.POST['title']
        photo = request.FILES.get('photo')
        body = request.POST['body']
        category = request.POST['category']

        new = News.objects.create(title=title, photo=photo, body=body, user=request.user)

        for cat in category:
            ct = Category.objects.get(id=cat)
            new.category.add(ct)
            return redirect('dashboard_url')