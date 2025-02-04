from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.mark_completed()  # Use the method from the model
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def overdue_tasks(request):
    tasks = Task.objects.filter(due_date__lt=timezone.now(), completed=False)
    return render(request, 'tasks/overdue_tasks.html', {'tasks': tasks})
