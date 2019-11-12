from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movie_pk>/score/new/', views.score_new, name='score_new'),
    path('<int:movie_pk>/edit/', views.edit, name='edit'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    #path('create/', views.create, name='create'),
    path('', views.index, name='index'),
]