from django.shortcuts import render ,HttpResponseRedirect ,reverse
from django.views import generic
from django.contrib.auth.models import User

from Company.forms  import SignUpForm as compSignupForm
from Company.forms  import SignUpUser as compSignupUser
from Company.models import Company ,CompanyProfile

from JobSeeker.forms import SignUpForm as jobSignupForm
from JobSeeker.forms import SignUpUser as jobSignupUser
from JobSeeker.models import JobSeeker,JobSeekerProfile

class Login(generic.TemplateView):
    template_name = "registration/login.html"

class signup(generic.TemplateView):
    template_name = "registration/signup.html"
    
    def post(self ,request ,*args, **kwargs):
        context = {}
        if request.POST['type'] == "company":            
            userForm = compSignupUser(request.POST)
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
                else:
                    context['compProfileForm'] = profileForm.errors
            else:
                context['compUserForm'] = userForm.errors
        else:
            userForm = jobSignupUser(request.POST)
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
                    return HttpResponseRedirect(reverse("login"))
                else:
                    context['jobProfileForm'] = profileForm.errors
            else:
                context['jobUserForm'] = userForm.errors
        return render(request ,template_name=self.template_name ,context=context)
