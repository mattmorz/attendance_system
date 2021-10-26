from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    TRANSGENDER = 'T'
    IRNS = 'I'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (TRANSGENDER, 'Transgender'),
        (IRNS, 'I\'d rather not say'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,null=False,blank=False)
    last_name = models.CharField(max_length=200,null=False,blank=False)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1,null=False,blank=False)
    date_of_birth = models.DateField(null=False,blank=False)

    def __str__(self):
        return self.last_name +', '+self.first_name

