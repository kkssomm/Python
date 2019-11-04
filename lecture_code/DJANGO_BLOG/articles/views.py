from django.shortcuts import render,redirect
from .models import Article, Comment

### CRUD

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

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title,content=content)
    # article.save()
    # return redirect('articles:detail',article.pk)

 
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title,content=content)
        article.save()
        return redirect('articles:detail',article.pk)
    else : 
        return render(request, 'articles/new.html')

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    comments = Comment.objects.filter(article=article)
    return render(request, 'articles/detail.html',{'article':article,'comments':comments})

def delete(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    return redirect('articles:index')

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     return render(request, 'articles/edit.html',{'article':article})

def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method =='POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail',article.pk)
    else:
        return render(request, 'articles/edit.html',{'article':article})



### REPLY

def comment_create(request,article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST.get('content')
        comment.article = article
        comment.save()
    #     return redirect('articles:detail', article_id)
    # else:
    #     return redirect('articles:detail',article_id)
    return redirect('articles:detail',article_id)

def comment_delete(request,article_id,comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
    return redirect('articles:detail',article_id)