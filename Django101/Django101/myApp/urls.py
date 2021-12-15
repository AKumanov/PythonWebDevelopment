from django.urls import path

from django.contrib import admin
from Django101.myApp.views import list_phones, blog_post

urlpatterns = [
    path('phones/', list_phones),
    path('blog/', blog_post),
]