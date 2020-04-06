from django.contrib import admin

from todo_list.models import TodoList
# Register your models here.

class TodoListAdmin(admin.ModelAdmin):
    list_display = ['task','completed']

admin.site.register(TodoList,TodoListAdmin)
