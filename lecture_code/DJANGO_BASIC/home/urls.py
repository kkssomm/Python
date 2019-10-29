from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('static_example/',views.static_example),
    path('/user_create/',views.user_create),
    path('/user_new/',views.user_new),
    path('/catch/',views.catch),
    path('/throw/',views.throw),
    path('/ispal/<word>/',views.ispal),
    path('/isbirth',views.isbirth),
    path('/square/<int:width>/<int:height>/', views.square),
    path('/introduce/<name>/<int:age>/', views.introduce),
    path('/hello/<name>/', views.hello),
    path('/lotto/', views.lotto),
    path('/dinner/', views.dinner),
    path('/hola/', views.hola),
    path('/index/', views.index),
    path('/admin/', admin.site.urls),
    path('/menu/',views.menu),
    path('/image/',views.image),
]
