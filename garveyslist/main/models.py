from django.db import models

# Create your models here.

class Business(models.Model):
    #business_type = models.ForeignKey('BusinessType', on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    zipcode = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    #owner = models.ForeignKey()


    def __str__(self):
        return self.name

    
class BusinessType(models.Model):
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name






