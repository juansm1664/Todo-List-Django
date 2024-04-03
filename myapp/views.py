from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    title = 'Django practics!!'
    return render(request,'index.html', {
        'title': title
    })

def about(request):
    username ='juanDa'
    return render(request,'about.html',{
        'username':username
    })

def hello(request, username):
    return HttpResponse("<h2>Hola Practicando Django %s</h2>" % username)

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects.html',{
        'projects': projects
    })

def tasks(request):
    # task = get_object_or_404
    tasks = Task.objects.all()
    return render(request, 'tasks.html',{
        'tasks': tasks 
    })