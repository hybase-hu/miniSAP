from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login_view(request):
    template = "base/login.html"

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")

    return render(request,template,context={})