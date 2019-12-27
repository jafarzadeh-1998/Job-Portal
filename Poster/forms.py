from django import forms

from . import models

class PosterForm(forms.ModelForm):
    class Meta:
        model = models.Poster
        fields = [ 'photo' ,'title' ,'expire' ,'salary' ,'work_hour' ,'poster_field' ]
        widgets = {
            'photo'     : forms.FileInput(attrs={"class":"form-control input-lg" ,'placeholder':"Photo" ,'name':"photo"}),
            'title'     : forms.TextInput(attrs={"class":"form-control input-lg" ,'placeholder':"Title" ,'name':"title"}),
            'expire'    : forms.DateInput(attrs={"class":"form-control input-lg" ,'placeholder':"Expire" ,'name':"expire"}),
            'salary'    : forms.TextInput(attrs={"class":"form-control input-lg" ,'placeholder':"Salery" ,'name':"salery"}),
            'work_hour' : forms.NumberInput(attrs={"class":"form-control input-lg" ,'placeholder':"Work Hour" ,'name':"work_hour"}),
        }

    def clean_photo(self):
        data = self.cleaned_data["photo"]
        
        return data

    def clean_title(self):
        data = self.cleaned_data["title"]
        
        return data
    
    def clean_expire(self):
        data = self.cleaned_data["expire"]
        
        return data
    
    def clean_salary(self):
        data = self.cleaned_data["salary"]
        
        return data
    
    def clean_work_hour(self):
        data = self.cleaned_data["work_hour"]
        
        return data
    
    def clean_poster_field(self):
        data = self.cleaned_data["poster_field"]
        
        return data
    