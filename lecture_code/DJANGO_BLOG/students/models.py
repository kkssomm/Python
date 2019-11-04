from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f'이름 : {self.name}'