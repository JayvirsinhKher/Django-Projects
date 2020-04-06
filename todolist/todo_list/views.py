from django.shortcuts import render,redirect
from todo_list.models import TodoList
from todo_list.forms import TodoListForm
from django.contrib import messages

# Create your views here.

def home_view(request):
    if request.method =='POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            comp = TodoList.objects.filter(completed=True)
            incomp = TodoList.objects.filter(completed=False)
            messages.success(request,('Task has been added to list!'))
            return render(request,'home.html',{'comp':comp,'incomp':incomp})
    else:
        comp = TodoList.objects.filter(completed=True)
        incomp = TodoList.objects.filter(completed=False)
        return render(request,'home.html',{'comp':comp,'incomp':incomp})

def delete(request,todolist_id):
    task  =TodoList.objects.get(pk=todolist_id)
    task.delete()
    messages.success(request,('Task has been deleted!'))
    return redirect('home')

def complete(request,todolist_id):
    task  =TodoList.objects.get(pk=todolist_id)
    task.completed = True
    task.save()
    return redirect('home')

def incomplete(request,todolist_id):
    task  =TodoList.objects.get(pk=todolist_id)
    task.completed = False
    task.save()
    return redirect('home')

def edit(request, todolist_id):
    if request.method =='POST':
        task = TodoList.objects.get(pk=todolist_id)

        form = TodoListForm(request.POST,instance = task)

        if form.is_valid():
            form.save()
            messages.success(request,('Task has been Edited!'))
            return redirect('home')
    else:
        task = TodoList.objects.get(pk=todolist_id)
        return render(request,'edit.html',{'task':task})
