from django.db import models

# Create your models here.
from django.db.models import TextField


class Student(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.firstname

class Goal(models.Model):
    goalname=models.CharField(max_length=100)
    subjectname = models.CharField( max_length=100 )
    targetrank = models.IntegerField()
    targetscore = models.IntegerField()
    targetdate = models.DateTimeField()
    currentscore = models.IntegerField()
    nameofexam =models.CharField(max_length=100)
    name=models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.nameofexam


