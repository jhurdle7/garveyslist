from django.shortcuts import render
from django.http import HttpResponse
from djano.models import Business 
from django.utils import timezone







# Create your views here.

def index(request):
    business = Business.objects.
    context = {'message': 'hello world!'
    'Business'

    }
    return render(request, 'main/index.html', context)