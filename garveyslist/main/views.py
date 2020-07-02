from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone







# Create your views here.
class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'businesses'

    def get_queryset(self):
        return Business.objects.fiter(pub_date_lte=timezone.now()).order_by('-pub_date')

def index(request):
    context = {'message': 'hello world!'


    }
    return render(request, 'main/index.html', context)