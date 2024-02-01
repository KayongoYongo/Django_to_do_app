from django.urls import path
from .views import task_list, add_task, update_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
]
