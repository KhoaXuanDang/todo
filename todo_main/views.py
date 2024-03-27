from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at') # fetch all data that task has not completed
    context = {
        'tasks': tasks,
    }
    return render(request, 'home.html', context)