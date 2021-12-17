from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Todo(models.Model):
    PRIORITY_URGENT = 'urgent'
    PRIORITY_NOT_URGENT = 'not urgent'

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    priority = models.CharField(
        max_length=200,
        default='not urgent',
        choices=(
            (PRIORITY_URGENT, 'urgent'),
            (PRIORITY_NOT_URGENT, 'not urgent')
        )
    )
