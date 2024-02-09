from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))

def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            messages.info(request, 'invalid login details')
            return redirect('login')
    
    else:
        return render(request, 'authentication.html')
    
def Signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if len(password)>6:
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'username is already registered')
                    return redirect('login')  
                
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'email is already registered')
                    return redirect('login') 
                 
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.backend = 'django.contrib.auth.backends.EmailOrUsernameModelBackend'
                    user.save()
                    authenticate_user = authenticate(request, username=username, password=password)
                    login(request, authenticate_user)
                    return HttpResponseRedirect(reverse_lazy('home'))
            else:
                messages.info(request, 'password mismatch')
                return redirect('login')    
        
        else:
            messages.info(request, 'password must be more than 6 digits')
            return redirect('login')