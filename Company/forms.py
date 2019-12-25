from django import forms
from django.contrib.auth.models import User

from . import models

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.CompanyProfile
        fields = [ 'name' ,'address' ,'phoneNumber' , 'dateOfFoundation' ]

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
    
class SignUpUser(forms.Form):
    username = forms.CharField(max_length=300)
    password = forms.CharField(max_length=300)
    confirm_password = forms.CharField(max_length=300)

    def clean_username(self):
        data = self.cleaned_data["username"]
        user = User.objects.filter(username=data).count()
        if user :
            raise forms.ValidationError('This username is already exist.')
        return data
    
    def clean_password(self):
        data = self.cleaned_data["password"]
        
        return data
    
    def clean_confirm_password(self):
        data = self.cleaned_data["confirm_password"]
        password = self.cleaned_data.get('password')
        if data != password:
            raise forms.ValidationError('Password doesn\'t match.')  
        
        return data
    