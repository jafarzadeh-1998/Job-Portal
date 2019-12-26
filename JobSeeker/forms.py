from django import forms
from django.contrib.auth.models import User

from . import models

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.JobSeekerProfile
        fields = [ 'firstName' ,'lastName' ,'age' ,'gender' ]
        widgets = { 
            'firstName'   : forms.TextInput(attrs={"class":"form-control input-lg" ,'placeholder':"firstName" ,'name':"firstName"}),
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
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.JobSeekerProfile
        fields = [ 'photo' ,'firstName' ,'lastName' ,'age' ,'grade',
                   'gender' ,'phoneNumber' ,'jobSeekField' ,'resume']
        widgets = { 
            'photo'       : forms.FileInput(attrs={"class":"form-control input-lg" ,'placeholder':"Photo" ,'name':"photo"}),
            'firstName'   : forms.TextInput(attrs={"class":"form-control input-lg" ,'placeholder':"First Name" ,'name':"firstName"}),
            'lastName'    : forms.TextInput(attrs={"class":"form-control input-lg" ,'placeholder':"Last Name" ,'name':"lastName"}),            
            'age'         : forms.NumberInput(attrs={'class':"form-control input-lg" ,'placeholder':"Age" ,'name':"age"}),
            'phoneNumber' : forms.TextInput(attrs={'class':"form-control input-lg" ,'placeholder':"Phone Number" ,'name':"phoneNumber"}),
            'resume'      : forms.FileInput(attrs={'class':"form-control input-lg" ,'placeholder':"Resume" ,'name':"resumer"}),
        }
    
    def clean_photo(self):
        data = self.cleaned_data["photo"]
        
        return data
    
    def clean_firstName(self):
        data = self.cleaned_data["firstName"]
        
        return data
    
    def clean_lastName(self):
        data = self.cleaned_data["lastName"]
        
        return data

    def clean_age(self):
        data = self.cleaned_data["age"]
        
        return data

    def clean_resume(self):
        data = self.cleaned_data["resume"]
        
        return data
   
    def clean_phoneNumber(self):
        data = self.cleaned_data["phoneNumber"]
        
        return data
    
    def clean_jobSeekField(self):
        data = self.cleaned_data["jobSeekField"]
        
        return data
    
    def clean_grade(self):
        data = self.cleaned_data["grade"]
        
        return data
    
    def clean_gender(self):
        data = self.cleaned_data["gender"]
        
        return data
    