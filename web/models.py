from django.db import models
from datetime import datetime


class Publication(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)


class Comments(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    pub = models.IntegerField()
