from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Business, BusinessType
from django.contrib.auth.decorators import login_required

from .forms import BusinessForm
from django.db.models import Q








# Create your views here.

# class IndexView(generic.ListView):
#     template_name = 'main/index.html'
#     context_object_name = 'businesses'

#     def get_queryset(self):
#         return Business.objects.fiter(pub_date_lte=timezone.now()).order_by('-pub_date')

def index(request):
    businesstypes = BusinessType.objects.all()

    page = request.GET.get('page', 1)
    search = ''
    if request.method == 'POST':
        search = request.POST['search']
        business = Business.objects.get(Q(businesstypes__icontains=search)
        | Q(name__icontains=search))
    
     
    context = {'title': 'Garveys List',
    'businesstypes': businesstypes,
    'search' : search

    }
    return render(request, 'main/index.html', context)



def detail(request, business_type):
    search = ''
    businesses = Business.objects.filter(types=business_type)
    businesstypes = BusinessType.objects.all()
     
    

    
    return render(request, 'main/detail.html', {'businesses': businesses, 'businesstypes': businesstypes})




@login_required
def addbusiness(request):
    businessform = BusinessForm()
    message = ''
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            form= BusinessForm()
        else:
            message= 'form is not valid'
    else:
        form = BusinessForm()
        
        
    return render(request, 'main/add.html', {'form': businessform, 'message:': message})



