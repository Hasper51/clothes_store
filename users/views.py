from django.shortcuts import render, redirect
from django.contrib import auth, messages
from users.models import User
from users.forms import UserLoginForm, UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('products:index')
    else:
        form = UserLoginForm()


    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('users:login')


    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:profile')

    else:
        form = UserEditForm(instance=request.user)
    context = {
        'title': 'Profile',
        'form': form
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect('products:index')