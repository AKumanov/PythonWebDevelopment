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


class Phone(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
