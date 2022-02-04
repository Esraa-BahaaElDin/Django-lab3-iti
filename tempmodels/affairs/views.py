from unicodedata import name
from django.shortcuts import render, redirect
from affairs.forms import TraineeForm1, TraineeForm2
from .models import myuser, Trainee, Track
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView

# Create your views here.


def register(req):
    context = {}
    if(req.method == 'GET'):
        return render(req, 'register.html')
    else:
        name = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']

        myuser.objects.create(name=name, password=password, email=email)
        User.objects.create_user(
            name=name, email=email, password=password, is_staff="True")
        return render(req, 'login.html', context)


def login(req):
    context = {}
    if(req.method == 'GET'):
        return render(req, 'login.html')
    else:
        username = req.POST['username']
        password = req.POST['password']
        authuser = authenticate(username=username, password=password)
        user = myuser.objects.filter(name=username, password=password)
        if(authuser is not None and user is not None):
            req.session['username'] = username
            auth_login(req, authuser)
            return render(req, 'home.html', context)
        else:
            context['msg'] = 'Invalid User'
            return render(req, 'login.html', context)


def logout(req):
    req.session['username'] = None
    auth_logout(req)
    return render(req, 'login.html')


def addtrainee(req):
    context = {}
    form = TraineeForm1()
    if (req.method == 'GET'):
        context['form'] = form
        return render(req, 'addtrainee.html', context)
    else:
        Trainee.objects.create(name=req.POST['name'],
                               bdate=req.POST['date'],
                               promotion=req.POST['promotion'],
                               intake=req.POST['intake'],
                               track=req.POST['track'])
        return render(req, 'home.html', context)


def inserttrainee(req):
    context = {}
    form = TraineeForm2()
    if (req.method == 'GET'):
        context['form'] = form
        return render(req, 'addtrainee.html', context)
    else:
        Trainee.objects.create(name=req.POST['name'],
                               bdate=req.POST['date'],
                               promotion=req.POST['promotion'],
                               intake=req.POST['intake'],
                               track=req.POST['track'])
        return render(req, 'home.html', context)


class trackcreateview(CreateView):
    model = Track
    fields = '__all__'


class tracklist(ListView):
    model = Track


























def home(req):
    context = {}
    if(req.method == 'GET'):
        context['trainees'] = Trainee.objects.all()
        return render(req, 'home.html', context)
    else:
        id = req.POST['id']
        name = req.POST['name']
        bdate = req.POST['date']
        promotion = req.POST['promotion']
        intake = req.POST['intake']
        track = req.POST['track']
        trainee = Trainee.objects.filter(
            name=name, bdate=bdate, promotion=promotion, id=id, intake=intake, track=track)

        return render(req, 'home.html', {'trainees': trainee})


def deletetrainee(req):
    if (req.method == 'GET'):
        return render(req, 'deletetrainee.html')
    else:
        traineeid = req.POST['id']
        trainee = Trainee.objects.filter(id=traineeid).delete()
        return redirect('/home', {'trainees': trainee})


def search(req):
    if (req.method == 'GET'):
        return render(req, 'search.html')
    else:
        name = req.POST['name']
        context = {}
        context['trainees'] = Trainee.objects.filter(name__icontains=name)
        return render(req, 'search.html', context)


def updatetrainee(req):
    if (req.method == 'GET'):
        return render(req, 'updatetrainee.html')
    else:
        traineeid = req.POST['id']
        updatedname = req.POST['name']
        updateddate = req.POST['date']
        updatedpromotion = req.POST['promotion']
        updatedintake = req.POST['intake']
        updatedtrack = req.POST['track']
        trainee = Trainee.objects.filter(id=traineeid).update(
            name=updatedname, bdate=updateddate, promotion=updatedpromotion, intake=updatedintake, track=updatedtrack)
        return redirect('/home', {'trainees': trainee})
