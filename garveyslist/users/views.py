from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request, 'users/home.html')

def login_page(request):
    if request.method == 'POST':

        username = request.POST['username']
        password =  request.POST['password']

        user = authenticate(request, username=username, password = password)
        if user is None: 
            return reder(request, 'users/login.html', {'message': ' there is no User with that name or password'})
            login(request, user)
            if 'next' in request.GET:
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('users:home'))

        return render(request, 'users/login.html')

def register_page(request):
    if request.method == 'POST':

        username - request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']

        if password != retype_password:
            return render(request, 'users/register.html', {'message:': 'passwords not match'})
        if User.objects.filter(username=username).exist():
            return render(request, 'users/register.html', {'message':' a user with that username already exist'})
        user - User.objects.create_user(username, email, passowrd)
        login(request, user)
        return render(request, user)

        return HttpResponseRedirect(reverse('users:home'))
        
    return render(request, 'users/register.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login_page'))