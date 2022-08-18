import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

# Create your views here.
from tasks.forms import TaskForm
from tasks.models import Task, TaskDetails


@login_required(login_url="login")
def all_task_views(request):
    tasks = Task.objects.filter(is_finished=False).order_by('deadline')
    finished_task = None
    # ha rendelkezik boss jogsival, a befejezetteket is listázzuk
    if request.user.groups.filter(name="boss").exists():
        finished_task = Task.objects.filter(is_finished=True).order_by('deadline')

    context = {
        'data': tasks,
        'finished_data':finished_task
    }
    template = "tasks/all_task_views.html"
    return render(request, template, context)


@login_required(login_url="login")
def my_tasks_list(request):
    tasks = Task.objects.filter(assigned_user=request.user,is_finished=False).order_by('deadline')

    finished_task = Task.objects.filter(assigned_user=request.user,is_finished=True).order_by('deadline')
    context = {
        'data': tasks,
        'finished_data': finished_task
    }
    template = "tasks/all_task_views.html"
    return render(request, template, context)


@login_required(login_url="login")
def task_view(request, id):
    task = Task.objects.get(id=id)
    is_my_task = task.assigned_user == request.user

    if is_my_task:
        if task.is_seen is not True:
            task.is_seen = True
            task.save()

    context = {
        'data': task,
        'is_my_task': is_my_task #ez nem is feltétlen kell
    }
    template = "tasks/task_view.html"
    return render(request, template, context)


@login_required(login_url="login")
def task_modify(request, id):
    if request.method == 'POST':
        user = request.user
        task = Task.objects.get(id=id)

        if "description" in request.POST:
            desc = request.POST["description"]
        else:
            desc = "modifyed assigned user"

        if task.assigned_user != request.user:
            messages.success(request,"Taker your owned process")
            task.is_assigned = True
            task.assigned_user = request.user

        if 'finished' in request.POST:
            if request.POST['finished'] == 'on':
                messages.success(request, "Your finished the process")
                task.is_finished = True
                task.finished_date = datetime.datetime.now()

        task.save()

        obj = TaskDetails.objects.create(
            task=task,
            user_id=user,
            modify_desc=desc
        )
        obj.save()
        messages.success(request, "Create new process")
        return redirect("tasks:task_view", id=id)


@login_required(login_url="login")
def add_new_task(request):
    if request.user.groups.filter(name='boss').exists():
        form = TaskForm()

        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                if task.assigned_user is not None:
                    task.is_assigned = True

                task.save()

                messages.success(request,"Saved the new task")
                return redirect("/")





        template = 'tasks/add_task.html'
        context = {
            'form':form
        }
        return render(request=request,template_name=template,context=context)
    else:
        messages.warning(request,"Not allowed this function for you")
        return redirect("/")
