from django.shortcuts import render
from Django101.myApp.models import Person, BlogPost, Phone


def index(request):
    context = {
        'name': 'Alexander',
        'people': Person.objects.all(),
        'posts': BlogPost.objects.all(),

    }
    return render(request, 'index.html', context)


def list_phones(request):
    context = {
        'phone': Phone.objects.all(),
    }
    return render(request, 'phones.html', context=context)


def blog_post(request):
    context = {
        'posts': BlogPost.objects.all()
    }
    return render(request, 'blog.html', context)
