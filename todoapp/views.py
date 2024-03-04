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

