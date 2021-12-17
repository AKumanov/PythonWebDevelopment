from django.urls import path

from todo_app.todo_application.views import index

urlpatterns = [
    path('', index)
]
