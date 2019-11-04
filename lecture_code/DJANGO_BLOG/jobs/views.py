from django.shortcuts import render
from faker import Faker
from .models import Job

def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    name = request.POST.get('name')

    # DB에 이름이 있는지 확인
    person = Job.objects.filter(name=name).first()
    # person = Job.objects.get(name=name)

    # 이미 같은 name이 있으면 기존 name의 past_life는 true
    if person:
        past_job = person.past_job
    else:
        faker = Faker('ko-KR')
        past_job = faker.job()
        person = Job(name=name,past_job=past_job)
        person.save()
    return render(request,'jobs/past_life.html',{'person':person})