from django.shortcuts import render ,HttpResponseRedirect ,reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms,models
from Company.models import Company

class Index(generic.DetailView):
    template_name='poster/poster-detail.html'
    model = models.Poster

class AddPost(LoginRequiredMixin ,generic.FormView):
    login_url = reverse_lazy('login')
    template_name = 'poster/createPoster.html'
    form_class = forms.PosterForm    
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        if Company.objects.filter(user=request.user).count() != 1 and request.user.is_authenticated:
            return HttpResponseRedirect(reverse('jobseeker:index'))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):        
        form = self.form_class(request.POST ,request.FILES)
        if form.is_valid():
            poster = models.Poster(company =request.user.company,
                                   photo=form.cleaned_data['photo'],
                                   title=form.cleaned_data['title'],
                                   expire=form.cleaned_data['expire'],
                                   salary=form.cleaned_data['salary'],
                                   work_hour=form.cleaned_data['work_hour'],
                                   poster_field=form.cleaned_data['poster_field'],
                                   )
            poster.save()
            return HttpResponseRedirect(reverse("poster:detail" ,args=[1]))        
        return super().post(request, *args, **kwargs)