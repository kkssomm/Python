from django.shortcuts import render, redirect
from .models import Movie

def index(request):
    movies = Movie.objects.order_by('-pk')
    return render(request, 'movies/index.html',{'movies':movies})

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    #scores = movie.s_set.order_bty('-pk')
    return render(request,'movies/detail.html',{'movie':movie})

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method=='POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)

def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.audience = request.POST.get('audience')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        return render(request, 'movies/edit.html', {'movie':movie})

def score_new(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if reuqest.method == 'POST':
        score = Score()
        score.content = request.POST.get('score')
        score.movie=movie
        score.save()
    return redirect('movies:detail',movie.pk)

def score_delete(request, movie_pk, score_pk):
    if request.method == 'POST':
        score = Score.objects.get(pk=score_pk)
        score.delete()
    return redirect('movies:detail', movie_pk) 