from django.contrib import admin

# Register your models here.
from .models import Business, BusinessType

admin.site.register(Business)
admin.site.register(BusinessType)