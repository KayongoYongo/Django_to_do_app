from django.shortcuts import render, redirect
from .models import Task

# Create your views here
def task_list(request):
    """
    This function deals with rendering all tasks onto the html form
    """
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    """
    This function deals with adding tasks to the database
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')

    return render(request, 'todo/add_task.html')
