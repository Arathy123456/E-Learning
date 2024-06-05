from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Userregistrations(models.Model):
    #  id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=200, unique=True, null=True)
    user_image = models.ImageField(upload_to='profiles')
    Password = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username


class Classroom(models.Model):
    date = models.DateField()
    duration = models.DurationField()
    topic = models.CharField(max_length=200)
    trainer_name = models.CharField(max_length=100)


class profile(models.Model):
    profile_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profiles')
