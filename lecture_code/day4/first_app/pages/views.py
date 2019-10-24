from django.shortcuts import render
from django.http import HttpResponse
import random
import datetime

def index(request):
    return render(request, 'index.html')

def match(request):
    chemi = random.randint(50,100)
    me = request.POST.get('me')
    you = request.POST.get('you')
    test = request.method
    context = {
        'me':me,
        'you':you,
        'chemi':chemi,
        'test':test,
    }
    return render(request, 'match.html', context)

def home(request):
    name = 'juan'
    data = ['A','B','C']
    empty_data = ['엄복동','클레멘타인','성냥팔이 소녀의 재림']
    matrix = [[1,2,3]],[[4,5,6]]
    context = {
        'name':name,
        'data':data,
        'empty_data':empty_data,
        'matrix':matrix,
        'number':10,
        'datetime':datetime,
    }

    return render(request,'home.html',context)

def lotto(request):
    lotto = sorted(random.sample(range(1,46),6))
    # context={
    #     'lotto':lotto,
    # }
    return render(request,'lotto.html',{'lotto':lotto})

def cube(request,num):
    cube = num ** 3
    context = { 
        'cube':cube,
        'num':num
    }
    return render(request,'cube.html',context)

def static_example(request):
    return render(request, 'static_example.html')
