from django import forms
from .models import Business, BusinessType


class BusinessForm(forms.ModelForm):
    class Meta:

        model = Business
        fields = '__all__'

       