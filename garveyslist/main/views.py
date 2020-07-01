from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'message': 'hello world!'

    }
    return render(request, 'main/index.html', context)