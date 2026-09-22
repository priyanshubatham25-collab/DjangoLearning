from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from .form import RegistrationForm

# Create your views here.
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request, user)
            messages.success(request,'Regisration successful👍')
            return redirect('login')
        else:
            messages.error(request,"Resgisraton failed please try again!")
            return render(request,'register.html',{'form':form})
    else:
        form = RegistrationForm()
        return render(request,'register.html' ,{'form':form})

def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"login success")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid username or password")
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    messages.success(request,'You have been logged out ')
    return redirect('register')

@login_required(login_url='login')      
def dashboard(request):
    return render(request,'dashboard.html')