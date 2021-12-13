from django.shortcuts import render
from Django101.myApp.models import Person, BlogPost


def index(request):
    context = {
        'name': 'Alexander',
        'people': Person.objects.all(),
        'posts': BlogPost.objects.all(),

    }
    return render(request, 'index.html', context)


def list_phones(request):
    context = {
        'phones': [
            {
                'name': 'Samsung Galaxy 500',
                'quantity': 5,
                'price': 800,
            },
            {
                'name': 'Motorolla XS',
                'quantity': 0,
                'price': 450,
            },
            {
                'name': 'iPhone 13 S',
                'quantity': 6,
                'price': 1000,
            }
        ]
    }
    return render(request, 'phones.html', context=context)
