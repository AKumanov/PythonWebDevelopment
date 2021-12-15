from django.contrib import admin

from Django101.myApp.models import Person, BlogPost, Phone

admin.site.register(Person)
admin.site.register(BlogPost)
admin.site.register(Phone)
