from django.contrib import admin

# Register your models here.
from todo_app.todo_application.models import Todo, Person


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'owner', 'priority']
    list_filter = ['owner']


# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('name', )


admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
