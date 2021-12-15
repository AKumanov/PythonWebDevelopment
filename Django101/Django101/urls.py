from django.contrib import admin
from django.urls import path, include

import Django101
from Django101.myApp import urls
from Django101.myApp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('', include('Django101.myApp.urls')),
    path('', include('Django101.myApp.urls')),

]
