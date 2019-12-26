from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(max_length=300,
                            widget=forms.TextInput(attrs={ 'class':"form-control input-lg" ,'placeholder':"username" ,'name':"username"}))
    password = forms.CharField(max_length=300,
                            widget=forms.PasswordInput(attrs={ 'class':"form-control input-lg" ,'placeholder':"Password" ,'name':"password"}))

    def clean_username(self):
        data = self.cleaned_data["username"]
        if User.objects.filter(username=data).count() != 1:
            raise forms.ValidationError("username doesn't match")
        return data
    
    def clean_password(self):
        data = self.cleaned_data["password"]
        username = self.cleaned_data.get('username')
        user = authenticate(username=username, password=data)
        if user is  None:
            raise forms.ValidationError("Password is wrong")
        return data

class SignUpUser(forms.Form):
    username = forms.CharField(max_length=300,
                            widget=forms.TextInput(attrs={"class":"form-control input-lg" ,'placeholder':"username(email)" ,'name':"username"}))
    password = forms.CharField(max_length=300,
                            widget=forms.PasswordInput(attrs={"class":"form-control input-lg" ,'placeholder':"password" ,'name':"password"}))
    confirm_password = forms.CharField(max_length=300,
                                    widget=forms.PasswordInput(attrs={"class":"form-control input-lg" ,'placeholder':"confirm_password" ,'name':"confirm_password"}))

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