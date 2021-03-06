from django import forms
from django.contrib.auth.models import User

from . import models

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.CompanyProfile
        fields = [ 'name' ,'phoneNumber' , 'dateOfFoundation' ,'address' ]
        widgets={
            'name'             : forms.TextInput(attrs={'class':"form-control input-lg" ,'placeholder':"Company Name" ,'name':"name"}),
            'phoneNumber'      : forms.TextInput(attrs={'class':"form-control input-lg" ,'placeholder':"Phone Number" ,'name':"phoneNumber"}),
            'dateOfFoundation' : forms.NumberInput(attrs={'class':"form-control input-lg" ,'placeholder':"dateOfFoundation" ,'name':"dateOfFoundation"}),
            'address'          : forms.Textarea(attrs={"name":"address" ,'class':"form-control input-lg" ,'placeholder':"Address" ,'cols':"30" ,'rows':"5"}),
        }   

    def clean_name(self):
        data = self.cleaned_data["name"]
        
        return data
    
    def clean_address(self):
        data = self.cleaned_data["address"]
        
        return data
    
    def clean_phoneNumber(self):
        data = self.cleaned_data["phoneNumber"]
        try:
            int(data)
        except ValueError:
            raise forms.ValidationError('It should be numeric.')

        if len(data) != 11:
            raise forms.ValidationError('It should be 11 digit.')
        return data
    
    def clean_dateOfFoundation(self):
        data = self.cleaned_data["dateOfFoundation"]

        return data
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.CompanyProfile
        fields = [ 'photo' ,'name' , 'dateOfFoundation' ,'job_field' ,'website',
                   'phoneNumber' ,'address' ]
        widgets={
            'photo'            : forms.FileInput(attrs={'name':'photo'}),
            'name'             : forms.TextInput(attrs={'class':"form-control input-lg" ,'placeholder':"Company Name" ,'name':"name"}),
            'phoneNumber'      : forms.TextInput(attrs={'class':"form-control input-lg" ,'placeholder':"Phone Number" ,'name':"phoneNumber"}),
            'dateOfFoundation' : forms.NumberInput(attrs={'class':"form-control input-lg" ,'placeholder':"dateOfFoundation" ,'name':"dateOfFoundation"}),
            'address'          : forms.Textarea(attrs={"name":"address" ,'class':"form-control input-lg" ,'placeholder':"Address" ,'cols':"30" ,'rows':"5"}),
            'job_field'        : forms.TextInput(attrs={'class':"form-control input-lg" ,'placeholder':"Job Field" ,'name':"job_field"}),
            'website'          : forms.TextInput(attrs={'class':"form-control input-lg" ,'placeholder':"Web Site" ,'name':"website"}),
        }

    def clean_photo(self):
        data = self.cleaned_data.get('photo')

        return data
    
    def clean_name(self):
        data = self.cleaned_data["name"]
        
        return data
    
    def clean_address(self):
        data = self.cleaned_data["address"]
        
        return data
    
    def clean_dateOfFoundation(self):
        data = self.cleaned_data["dateOfFoundation"]
        
        return data
    
    def clean_job_field(self):
        data = self.cleaned_data["job_field"]
        
        return data
    
    def clean_website(self):
        data = self.cleaned_data["website"]
        
        return data
    
    def clean_phoneNumber(self):
        data = self.cleaned_data["phoneNumber"]
        try:
            int(data)
        except ValueError:
            raise forms.ValidationError('It should be numeric.')

        if len(data) != 11:
            raise forms.ValidationError('It should be 11 digit.')
        return data