from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json
from .models import Task


# Create your views here
def task_list(request):
    """
    This function returns all the tasks in JSON format.
    """

    tasks = Task.objects.all()
    return render(request, 'todo_app/task_list.html', {'tasks':tasks})

def find_task(request, task_id):
    """
    This function returns a single task in JSON format.
    If the task is not found, it returns an error 404
    """
    
    tasks = get_object_or_404(Task, id=task_id)
    return render(request, 'todo_app/update_task.html', {'tasks':tasks})
    
def add_task(request):
    """
    This function deals with adding tasks to the database
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')

    return render(request, 'todo_app/add_task.html')

def update_task(request, task_id):
    """
    Description: This function edits the task and
    shows whether it is updated or not.

    Args: request
    """
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        completed = request.POST.get('completed', False) == 'on'
        task.title = title
        task.completed = completed
        task.save()
        return redirect('task_list')
    
    return render(request, 'todo_app/update_task.html', {'task': task})

def delete_task(request, task_id):
    """
    Description: This dunction deletes tasks.

    Args:
        request
        task_id
    """
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
