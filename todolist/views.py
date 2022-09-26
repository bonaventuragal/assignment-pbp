from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from todolist.models import Task
from todolist.forms import TaskForm
import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def todolist(req):
    list_task = Task.objects.filter(user=req.user)
    context = {
        'list_task': list_task,
        'username': req.user.username
    }
    return render(req, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task(req):
    if req.method == "POST":
        form = TaskForm(req.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            Task.objects.create(title=title, description=description, date=datetime.datetime.now(), user=req.user)
            return redirect('todolist:todolist')
    else:
        form = TaskForm()

    return render(req, "add_task.html", context={"form": form})

@login_required(login_url='/todolist/login/')
def change_status(req, id):
    task = Task.objects.get(id=id)
    task.is_finished = not(task.is_finished)
    task.save()
    return redirect('todolist:todolist')

@login_required(login_url='/todolist/login/')
def delete(req, id):
    Task.objects.get(id=id).delete()
    return redirect('todolist:todolist')

def register(req):
    form = UserCreationForm()

    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(req, 'register.html', context)

def login_user(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            response = HttpResponseRedirect(reverse("todolist:todolist")) # membuat response
            # response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(req, 'Username atau Password salah!')
    context = {}
    return render(req, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response