
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import *


def index(request):
    return render(request, 'base/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, "base/signup.html", {'form': form})