from django.shortcuts import render,redirect
from .models import Article

# Create your views here.
def index(request):
    #articles = Article.objects.order_by('-pk')
    articles = Article.objects.all()[::-1]
    return render(request,'articles/index.html',{'articles':articles})

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # # 2
    # article = Article(title=title,content=content)
    # article.save()

    # # 3
    # Article.objects.create(title=title,content=content)

    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title,content=content)
    article.save()
    return redirect(f'/articles/{article.pk}/')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/detail.html',{'article':article})