from django.db import models

# Create your models here.

class Business(models.Model):
    business_type = models.ForeignKey
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    rating = models.IntegerField()
    
class BusinessType():
    name = models.CharField(max_length=200)





