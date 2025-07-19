from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == "POST":
        username = request.POST["Username"]
        password = request.POST['Password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Invalid Username or Password. Please Try Again!"
            return render(request, 'signin.html', {'error': error})
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect(signin)