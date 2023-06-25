from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm()
    return render(request, 'todos/create_todo.html', {'form': form})

def edit_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todos/edit_todo.html', {'form': form, 'todo': todo})

def delete_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todos/delete_todo.html', {'todo': todo})
