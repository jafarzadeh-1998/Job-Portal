from django.shortcuts import render ,HttpResponseRedirect ,reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from . import forms

from Company.forms  import SignUpForm as compSignupForm
from Company.models import Company ,CompanyProfile

from JobSeeker.forms import SignUpForm as jobSignupForm
from JobSeeker.models import JobSeeker,JobSeekerProfile

class Index(generic.TemplateView):
    template_name = "index.html"

class Login(generic.FormView):
    template_name = "registration/login.html"
    form_class = forms.LoginForm    
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
        return super().post(request, *args, **kwargs)

def Logout(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    logout(request)
    return HttpResponseRedirect(reverse("index"))

class signup(generic.TemplateView):
    template_name = "registration/signup.html"
    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['jobSeekerForm'] = jobSignupForm
        context['companyForm'] = compSignupForm
        context['userForm'] = forms.SignUpUser
        return context

    def post(self ,request ,*args, **kwargs):
        print(request.POST)
        context = self.get_context_data()
        if request.POST['type'] == "company":            
            userForm = forms.SignUpUser(request.POST)
            if userForm.is_valid():
                profileForm = compSignupForm(request.POST)
                if profileForm.is_valid():
                    'name' ,'address' ,'phoneNumber' , 'dateOfFoundation'
                    user = User(username=userForm.cleaned_data['username'])
                    user.set_password(userForm.cleaned_data['password'])
                    user.save()
                    company = Company(user=user)
                    company.save()
                    profile = CompanyProfile(company=company,
                                             name=profileForm.cleaned_data['name'],
                                             address=profileForm.cleaned_data['address'],
                                             phoneNumber=profileForm.cleaned_data['phoneNumber'],
                                             dateOfFoundation=profileForm.cleaned_data['dateOfFoundation'],
                                             )         
                    profile.save()
                    return HttpResponseRedirect(reverse("index"))
                else:
                    context['compProfileForm'] = profileForm.errors
            else:
                context['compUserForm'] = userForm.errors
        else:
            userForm = forms.SignUpUser(request.POST)
            if userForm.is_valid():
                profileForm = jobSignupForm(request.POST)
                if profileForm.is_valid():                    
                    user = User(username=userForm.cleaned_data['username'])
                    user.set_password(userForm.cleaned_data['password'])
                    user.save()
                    jobseeker = JobSeeker(user=user)
                    jobseeker.save()
                    profile = JobSeekerProfile(jobseeker=jobseeker,
                                               firstName=profileForm.cleaned_data['firstName'],
                                               lastName=profileForm.cleaned_data['lastName'],
                                               age=profileForm.cleaned_data['age'],
                                               gender=profileForm.cleaned_data['gender'],
                                            )
                    profile.save()
                    return HttpResponseRedirect(reverse("index"))
                else:
                    context['jobProfileForm'] = profileForm.errors
            else:
                context['jobUserForm'] = userForm.errors
        return render(request ,template_name=self.template_name ,context=context)
