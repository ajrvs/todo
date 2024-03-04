from django.shortcuts import render, redirect

from .models import *
from .forms import *

def home(request):
    # Retrieve all tasks from the database
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    
    context = {"tasks":tasks, "form":form} # dictionary
    return render(request, "home.html", context)

# Update task
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form":form}
    return render(request, "update_task.html", context)

# Delete task
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect("/")
    context = {"task":task}
    return render(request, "delete.html", context)