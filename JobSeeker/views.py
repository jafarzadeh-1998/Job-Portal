from django.shortcuts import render ,HttpResponseRedirect ,reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models ,forms

class Index(LoginRequiredMixin ,generic.TemplateView):
    login_url = reverse_lazy('login')
    template_name = "jobseeker/jobseeker_detail.html"
    model = models.JobSeeker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = models.JobSeeker.objects.filter(user=self.request.user).first().jobseekerprofile
        return context

    def get(self, request, *args, **kwargs):
        jobseeker = models.JobSeeker.objects.filter(user=request.user)
        if jobseeker.count() == 0:
            return HttpResponseRedirect(reverse('index'))
        return super().get(request, *args, **kwargs)


class Profile(LoginRequiredMixin ,generic.TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'jobseeker/editProfile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context["form"] = forms.ProfileForm(instance=self.request.user.jobseeker.jobseekerprofile)
        return context
    
    def get(self, request, *args, **kwargs):
        jobseeker = models.JobSeeker.objects.filter(user=request.user)
        if jobseeker.count() == 0:
            return HttpResponseRedirect(reverse('index'))
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):        
        form = forms.ProfileForm(request.POST ,request.FILES)
        jobseeker = models.JobSeeker.objects.filter(user=request.user).first()
        profile = jobseeker.jobseekerprofile
        if form.is_valid():
            profile.photo        = form.cleaned_data['photo']
            profile.firstName    = form.cleaned_data['firstName']
            profile.lastName     = form.cleaned_data['lastName']
            profile.gender       = form.cleaned_data['gender']
            profile.grade        = form.cleaned_data['grade']
            profile.phoneNumber  = form.cleaned_data['phoneNumber']
            profile.age          = form.cleaned_data['age']
            profile.resume       = form.cleaned_data['resume']
            profile.jobSeekField = form.cleaned_data['jobSeekField']
            profile.save()
        else:            
            return HttpResponseRedirect(reverse('jobseeker:editProfile'))
        return HttpResponseRedirect(reverse('jobseeker:index'))