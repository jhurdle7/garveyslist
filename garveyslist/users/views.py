from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from main.models import Business, BusinessType





#from django.apps import main

# Create your views here.

@login_required
def user(request):
    print(request.user.username)
    return render(request, 'users/user.html')

def login_page(request):
    search = ''
    #businesses = Business.objects.filter(types=business_type)
    businesstypes = BusinessType.objects.all()
     
        
    if request.method == 'POST':
        print(request.POST)

        username = request.POST['username']
        password =  request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is None: 
            return render(request, 'users/login.html', {'message': ' there is no User with that name or password'})
        login(request, user)
        if 'next' in request.GET:
            return HttpResponseRedirect(request.GET['next'])
        return HttpResponseRedirect(reverse('users:user'))

    return render(request, 'users/login.html',{'businesstypes': businesstypes})

def register_page(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']

        if password != retype_password:
            return render(request, 'users/register.html', {'message:': 'passwords do not match'})
        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'message':' a user with that username already exist'})
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return render(request, 'users/user.html')

        return HttpResponseRedirect(reverse('users:users'))
        
    return render(request, 'users/register.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))


