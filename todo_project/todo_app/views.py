from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json
from .models import Task


# Create your views here
def task_list(request):
    """
    This function deals with rendering all tasks onto the html form
    """

    tasks = Task.objects.all()
    # tasks_json = serializers.serialize('json', tasks)
    tasks_json = [{'title': task.title} for task in tasks]
    return JsonResponse(tasks_json, safe=False)
    # return HttpResponse(tasks_json, content_type='application/json')
    # return render(request, 'todo_app/task_list.html', {'tasks': tasks})

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
