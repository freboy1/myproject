from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, user=form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('posts:list')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def my_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:list')
    