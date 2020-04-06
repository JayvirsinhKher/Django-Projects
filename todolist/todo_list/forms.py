from django import forms
from todo_list.models import TodoList

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        # fields='__all__'
        fields = ['task','completed']
