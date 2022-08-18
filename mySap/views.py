from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render


def login_view(request,*args,**kwargs):
    template = "base/login.html"
    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect("tasks:home")

    return render(request=request,template_name='base/login.html')


@login_required(login_url='login')
def logout_view(request):
    user = request.user
    print("---------")
    if user is not None:
        logout(request)
        return redirect("login")
