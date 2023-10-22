from django.shortcuts import render,redirect
from .forms import CustomUserCreation
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomeUser
from .forms import AuthenticationForm,EditProfile



def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        form = AuthenticationForm()
        return render(request,'registration/login.html', context={'form': form})
    elif request.method == 'POST': 
        email = request.POST.get('email')
        password = request.POST.get('password')      
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid email or password')
            return redirect(request.path_info)

@login_required
def Logout(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        form = CustomUserCreation()
        return render(request,'registration/signup.html', context={'form': form})
    else:
        form = CustomUserCreation(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            password = request.POST.get('password1')
            user = authenticate(email=email, password=password)
            login(request,user)
            return redirect('accounts:profile')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid email or password')
            return redirect(request.path_info)
        

def edit_profile(request):
    if request.method == 'GET':
        form = EditProfile()
        return render(request,'registration/edit_profile.html', context={'form': form})
    elif request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)
        form.is_valid()
        form.save()
        request.user.is_verified = True
        request.user.save()
        context ={
            'form': form,
        }
    return render(request,'registration/edit_profile.html', context={'form': form})


# Create your views here.