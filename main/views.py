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
        print('post keldi')
        title = request.POST['title']
        print(title)
        photo = request.FILES.get('photo')
        body = request.POST['body']
        category = request.POST['category']
        print(category)

        new = News.objects.create(title=title, photo=photo, body=body, user=request.user)

        for cat in category:
            try:
                ct = Category.objects.get(id=cat)
                new.category.add(ct)
                print(True)
            except:
                pass
