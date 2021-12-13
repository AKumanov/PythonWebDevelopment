from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    home_town = models.CharField(max_length=20)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=20)
    description = models.TextField()
    content = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=True)
