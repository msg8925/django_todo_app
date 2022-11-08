from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):

    # Get all tasks from task table
    tasks = Task.objects.all()

    # Pass tasks to template
    context = {
        "tasks": tasks
    }

    return render(request, 'todo/home.html', context)