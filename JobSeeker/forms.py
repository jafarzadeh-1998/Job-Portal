from django import forms
from django.contrib.auth.models import User

from . import models

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.JobSeekerProfile
        fields = [ 'firstName' ,'lastName' ,'age' ,'gender' ]
        widgets = { 
            'firstName' : forms.TextInput(attrs={"class":"form-control input-lg" ,'placeholder':"firstName" ,'name':"firstName"}),
            'lastName'  : forms.TextInput(attrs={"class":"form-control input-lg" ,'placeholder':"lastName" ,'name':"lastName"}),            
            'age'       : forms.NumberInput(attrs={'class':"form-control input-lg" ,'placeholder':"Age" ,'name':"age"})
        }

    def clean_name(self):
        data = self.cleaned_data["name"]
        
        return data
    
    def clean_address(self):
        data = self.cleaned_data["address"]
        
        return data
    
    
    def clean_dateOfFoundation(self):
        data = self.cleaned_data["dateOfFoundation"]

        return data
    