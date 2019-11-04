from django.db import models

class Timetable(models.Model):
    code = models.CharField(max_length=20)
    lecture = models.CharField(max_length=20)
    professor = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    dayofweek = models.CharField(max_length=10)

    def __str__(self):
        return f'강의 : {self.lecture}'
