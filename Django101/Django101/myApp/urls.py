from django.urls import path

from Django101.myApp.views import list_phones

urlpatterns = [
    path('', list_phones)
]