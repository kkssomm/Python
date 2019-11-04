from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def index(request):
    #articles = Article.objects.order_by('-pk')
    students = Student.objects.all()[::-1]
    return render(request,'students/index.html',{'students':students})