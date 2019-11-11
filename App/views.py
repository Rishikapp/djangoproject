from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Abc
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):
    return HttpResponse("Hellow world")


# Create your views here.

def home(request):
    objects = Abc.objects.all()
    recent = Abc.objects.order_by('-Date')[0:3]
    p = Paginator(objects, 2)
    return render(request, 'marketing-index.html', {'ob': objects, 're': recent})


def my(request):
    if request.method == 'POST':
        a = request.POST['Username']
        b = request.POST['Password']
        print(type(a), type(b))
        user = auth.authenticate(username=a, password=b)
        print(user, 'user is ************')
        if user is not None:
            auth.login(request, user)
            return redirect('App:home')
        else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect('App:login')
        # return render(request, 'marketing-index.html')
        # return redirect('App:home')
    return render(request, 'login.html')


def log(request):
    auth.logout(request)
    return redirect('App:home')


def register(request):
    if request.method == 'POST':
        a = request.POST['First name']
        b = request.POST['Last name']
        c = request.POST['Email Id']
        d = request.POST['Username']
        e = request.POST['Password']
        f = request.POST['Confirm Password']
        if e == f:
            if User.objects.filter(username=d).exists():
                messages.error(request, 'Username already exists')
                return redirect('App:register')
            elif User.objects.filter(email=c).exists():
                messages.error(request, 'Email already exists')
                return redirect('App:register')
            else:
                v = User.objects.create_user(first_name=a, last_name=b, username=d, password=e, email=c, is_staff=True, is_superuser=True)
                v.save()
                auth.login(request, v)
                messages.success(request, 'Registration successfull')
        else:
            messages.error(request, 'Password doesnot match')
            return redirect('App:register')
        return redirect('App:home')
    return render(request, 'register.html')



