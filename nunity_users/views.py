# views.py
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user-login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def logout_confirm(request):
    return render(request,'accounts/logout.html')