from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.utils import timezone
from .models import Task
from django.contrib.auth.models import User

import datetime
import json

# Create your views here.



def logoutUser(request):
    logout(request)
    return redirect('/login')  


@login_required
def index(request):
    # Obtém o usuário logado
    user = request.user

    status_filter = request.GET.get('status', '')
    user_filter = request.GET.get('user', '')

    if user.is_superuser:
        tasks = Task.objects.all()
        if status_filter:
            tasks = tasks.filter(status=status_filter)
        if user_filter:
            tasks = tasks.filter(assigned_to_id=user_filter)
        users = User.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=user)
        if status_filter:
            tasks = tasks.filter(status=status_filter)
        users = User.objects.filter(id=user.id)

    context = {
        'tasks': tasks,
        'users': users,
    }
    return render(request, 'index.html', context)

@login_required

def update_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')

        try:
            task = Task.objects.get(id=task_id)
            task.title = title
            task.description = description
            task.status = status
            task.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
        except Task.DoesNotExist:
            messages.error(request, 'Tarefa não encontrada!')

    return redirect('index')  

@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        assigned_to_id = request.POST.get('assigned_to')

        try:
            assigned_to = User.objects.get(id=assigned_to_id)
            Task.objects.create(
                title=title,
                description=description,
                status=status,
                assigned_to=assigned_to
            )
            messages.success(request, 'Tarefa criada com sucesso!')
        except User.DoesNotExist:
            messages.error(request, 'Usuário não encontrado!')

    return redirect('index')

@login_required
def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            messages.success(request, 'Tarefa excluída com sucesso!')
        except Task.DoesNotExist:
            messages.error(request, 'Tarefa não encontrada!')

    return redirect('index')

@login_required
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Usuário adicionado com sucesso!')
            # Optionally log in the new user automatically
            login(request, user)
        except Exception as e:
            messages.error(request, f'Erro ao adicionar usuário: {str(e)}')

    return redirect('index')


