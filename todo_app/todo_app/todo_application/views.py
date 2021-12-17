from django.shortcuts import render


# Create your views here.
from todo_app.todo_application.models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'index.html', context=context)
