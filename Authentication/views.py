from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

#Create your views here.
def home(request):
    return render(request,"Authentication/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        Fname = request.POST['Fname']
        Lastname = request.POST['Lastname']
        Email = request.POST['Email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myUser = User.objects.create_user(username, Email,pass1)
        myUser.Firstname = Firstname
        myUser.Lastname = Lastname

        myUser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('signin')

    return render(request,"Authentication/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            Firstname = user.Fname
            return render(request, "Authentication/index.html",{'Firstname':Fname})
        
        else:
            messages.error(request, "Bad credentials")
            return redirect('home')
         
    return render(request,"Authentication/signin.html")

def signout(request):
    pass