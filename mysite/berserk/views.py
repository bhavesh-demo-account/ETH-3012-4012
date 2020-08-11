from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for ' + user)
            return redirect('navigation')
    context = {'form': form}
    return render(request, 'berserk/registration.html', context)

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request)
            return redirect('registration')
        else:
            messages.info(request,'Username or Password is incorrect!')

    context = {}
    return render(request,'berserk/login.html', context)

def navigation(request):
    return render(request,'berserk/navigation.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

