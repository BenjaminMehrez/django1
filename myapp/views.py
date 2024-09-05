from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Project
from .forms import CreateNewTask, CreateNewProject


# Create your views here.

def index(req):
    title = 'Django Course!!'
    return render(req, 'index.html', {
        'title': title
    })


def about(req):
    return render(req, 'about.html')


def hello(req, username):
    return HttpResponse('<h1>Hello %s</h1>' % username)


def project(req):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(req, 'projects/projects.html', {
        'projects': projects
    })


def taskAll(req):
    # task = list(Task.objects.values())
    tasks = Task.objects.all()
    return render(req, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(req):
    if req.method == 'GET':
        return render(req, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=req.POST['title'], description=req.POST['description'], project_id=1)
        return redirect('tasks')


def create_project(req):
    if req.method == 'GET':
        return render(req, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=req.POST['name'])
        return redirect('projects')

def project_detail(req, id):
    product = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(req, 'projects/detail.html', {
        'product': product,
        'tasks': tasks
    })

