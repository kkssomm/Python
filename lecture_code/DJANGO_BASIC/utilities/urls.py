from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('translated/',views.translated),
    path('papago/',views.papago),
    path('',views.index),
]