from django.contrib.auth import authenticate
from django.core.mail import message
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('accounts:login')
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['pswd1']
        password2 = request.POST['pswd2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "An User With This Username already exists!!!")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "An User With This email is already registered!!!")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                password=password1, username=username)
                user.save()
                print("\n--- User Created ---\n")
        else:
            messages.info(request, "Passwords Donot match")

        return redirect('/')