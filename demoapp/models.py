from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 200)  
    last_name = models.CharField(max_length = 200)  
    roll_number = models.IntegerField() 

    def __str__(self):
        return self.first_name 


class State(models.Model):
    statename=models.CharField(max_length=50)
    statecode=models.CharField(max_length=2)

    def __str__(self):
        return self.statename

class City(models.Model):
    cityname=models.CharField(max_length=30)
    citystate=models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.cityname        