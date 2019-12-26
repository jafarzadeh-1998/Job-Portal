from django.shortcuts import render ,HttpResponseRedirect ,reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

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

class Profile(generic.TemplateView):
    template_name = 'company/editProfile.html'