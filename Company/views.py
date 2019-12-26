from django.shortcuts import render ,HttpResponseRedirect ,reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models ,forms

class Index(LoginRequiredMixin ,generic.TemplateView):
    login_url = reverse_lazy('login')
    template_name = "company/company-detail.html"
    model = models.Company

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = models.Company.objects.filter(user=self.request.user).first()        
        return context

    def get(self, request, *args, **kwargs):
        company = models.Company.objects.filter(user=request.user)
        if company.count() == 0:
            return HttpResponseRedirect(reverse('index'))
        return super().get(request, *args, **kwargs)

class CompanyList(generic.ListView):
    template_name = "company/companies.html"
    model = models.CompanyProfile
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context    

class Profile(LoginRequiredMixin ,generic.TemplateView):
    template_name = 'company/editProfile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = forms.ProfileForm(instance=self.request.user.company.companyprofile)
        return context
    
    def get(self, request, *args, **kwargs):
        company = models.Company.objects.filter(user=request.user)
        if company.count() == 0:
            return HttpResponseRedirect(reverse('index'))
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = forms.ProfileForm(request.POST ,request.FILES)
        company = models.Company.objects.filter(user=request.user).first()
        profile = company.companyprofile
        if form.is_valid():
            profile.photo            = form.cleaned_data['photo']
            profile.name             = form.cleaned_data['name']
            profile.address          = form.cleaned_data['address']
            profile.job_field        = form.cleaned_data['job_field']
            profile.website          = form.cleaned_data['website']
            profile.phoneNumber      = form.cleaned_data['phoneNumber']
            profile.dateOfFoundation = form.cleaned_data['dateOfFoundation']
            profile.save()
        return HttpResponseRedirect(reverse('company:profile'))