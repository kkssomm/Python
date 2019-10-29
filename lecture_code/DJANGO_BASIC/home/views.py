from django.shortcuts import render, HttpResponse
import random
import requests # pip install requests
from pprint import pprint as pp
from datetime import datetime

def index(request):
    # return HttpResponse('Welcome to Django')
    return render(request, 'home/index.html')

def hola(request):
    # return HttpResponse('Hello, my name in juan')
    return render(request, 'home/hola.html')

def dinner(request):
    menus = ['피자','치킨','족발','라면']
    dinner = random.choice(menus)
    # return HttpResponse(f'오늘의 저녁메뉴는 {dinner}입니다.')
    return render(request, 'home/dinner.html', {'menus':menus, 'dinner':dinner})

def lotto(request):
    numbers = range(1,46)
    my_lotto = random.sample(numbers, 6)  

    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=882"

    res = requests.get(url)
    data = res.json()
    # pp(data)

    winner = []
    for i in range(1,7):
        winner.append(data[f'drwtNo{i}'])

    match = set(my_lotto) & set(winner)
    rank = len(match)
    cnt = 1

    while rank < 5:
        cnt += 1
        my_lotto = random.sample(range(1,46),6)
        match = set(my_lotto) & set(winner)
        rank = len(match)
    return render(request, 'lotto.html', {'cnt':cnt, 'winner':winner, 'my_lotto':my_lotto})
# return HttpResponse(f'오늘의 로또 추천번호는 {my_lotto}입니다.')

# Variable Routing

def hello(request, name):
    return render(request, 'home/hello.html', {'name':name})

def introduce(request, name, age):
    return render(request, 'home/introduce.html', {'name':name, 'age':age})

def square(request, width, height):
    sq = width * height
    return render(request, 'home/square.html', {'width':width, 'height':height, 'sq':sq})

def menu(request):
    menus = ['아메리카노','라떼','카푸치노','모카','카라멜마끼아또']
    cafes = []
    my_sentence = []
    empty_list = []
    context = {
        'menus' : menus,
        'cafes':cafes,
        'my_sentence':my_sentence,
        'empty_list':empty_list,

    }
    return render(request,'home/template_language.html',context)

def image(request):
    return render(request,'home/image.html')

def isbirth(request):
    today = datetime.now()
    if today.month == 6 and today.day == 27:
        result = True
    else :
        result = False
    return render(request, 'home/isbirth.html',{'result':result})

##글자의 순서를 뒤집어도 원래의 글자가 되는 글자가 입력되면 회문이라고 표시, 아니며 아님 표시
def ispal(request,word):
    check = True
    if word == word[::-1]:
        check = True
    else :
        check = False
    render(request,'ispal.html',{'check':check})

def throw(request):
    return render(request, 'home/throw.html')

def catch(request):
    message = request.GET.get('message')
    return render(request,'home/catch.html',{'message':message})

def user_new(request):
    return render(request, 'home/user_new.html')

def user_create(request):
    user_name= request.POST.get('name')
    user_password = request.POST.get('pwd')
    return render(request,'home/user_create.html',{'user_name':user_name,'user_password':user_password})

def static_example(request):
    return render(request,'home/static_example.html')