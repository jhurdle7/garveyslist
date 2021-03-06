from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


    
class BusinessType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name





class Business(models.Model):
     
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=40, blank=True)
    owner = models.CharField(max_length=250)
    website = models.CharField(max_length=200, blank=True)
    comments = models.CharField(max_length=200)
    
    types = models.ManyToManyField(BusinessType, related_name='businesses')

    def __str__(self):
        return self.name



'''
business = Business.objects.get(id=1)
print(business.types.all())

business_type = BusinessType.objects.get(name='restaurant')
# print(business_type.business_set.all())
print(business_type.businesses.all())
'''



