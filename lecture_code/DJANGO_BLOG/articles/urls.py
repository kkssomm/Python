from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.detail),
    path('new/',views.new),
    path('create/',views.create),
    path('', views.index),
]