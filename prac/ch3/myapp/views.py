from django.shortcuts import render,redirect
from .models import Timetable


# Create your views here.
def index(request):
    courses = Timetable.objects.all()
    return render(request,'myapp/index.html',{'courses':courses})