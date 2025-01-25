# filepath: /d:/Django todo app/app/todo_app/tasks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
import socket

def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    vm_name = socket.gethostname()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'vm_name': vm_name})

def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if task_name:
            Task.objects.create(name=task_name, status='new')
            return redirect('task_list')
    return render(request, 'tasks/task_form.html')

def update_task_status(request, task_id, status):
    task = get_object_or_404(Task, id=task_id)
    task.status = status
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if task_name:
            task.name = task_name
            task.save()
            return redirect('task_list')
    return render(request, 'tasks/edit_task.html', {'task': task})