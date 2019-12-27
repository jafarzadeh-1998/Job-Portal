from django.shortcuts import render ,HttpResponseRedirect ,reverse ,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from . import forms,models
from Company.models import Company
from JobSeeker.models import JobSeeker

class Index(generic.DetailView):
    template_name='poster/poster-detail.html'
    model = models.Poster

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        poster = kwargs['object']
        try:
            poster.photo.url
            context['photo'] = poster.photo
            context['photoState'] = True
        except:
            pass
        return context

class ListPoster(generic.ListView):
    template_name = "poster/poster-list.html"
    model = models.Poster
    paginate_by = 5

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
        
class AddPoster(LoginRequiredMixin ,generic.FormView):
    login_url = reverse_lazy('login')
    template_name = 'poster/createPoster.html'
    form_class = forms.PosterForm    
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        if Company.objects.filter(user=request.user).count() != 1 and request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
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
            return HttpResponseRedirect(reverse("poster:detail" ,args=[poster.pk]))        
        return super().post(request, *args, **kwargs)

class EditPoster(LoginRequiredMixin ,generic.FormView):
    login_url = reverse_lazy('login')
    template_name = 'poster/editPoster.html'
    form_class = forms.PosterForm
    pk = None
    success_url = reverse_lazy('poster:detail' ,args=[pk]) 

    def get(self, request, *args, **kwargs):
        if Company.objects.filter(user=request.user).count() != 1 and request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        pk = kwargs['pk']
        poster = models.Poster.objects.filter(pk=pk).first()
        if poster.company != request.user.company:
            return HttpResponseRedirect(reverse('index'))
        self.pk = pk
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poster = models.Poster.objects.filter(company=self.request.user.company).first()
        context["form"] = self.form_class(instance=poster)
        try:
            poster.photo.url            
            context['photo'] = poster.photo
            context['photoState'] = True
        except:
            pass
        return context
    
    def get_success_url(self):
        return HttpResponseRedirect(reverse('poster:detail' ,args=[self.pk]))
    
    def post(self, request, *args, **kwargs):
        poster = models.Poster.objects.filter(pk=kwargs['pk']).first()
        form = forms.PosterForm(request.POST ,request.FILES)
        if form.is_valid():            
            poster.photo        = form.cleaned_data['photo']
            poster.title        = form.cleaned_data['title']
            poster.expire       = form.cleaned_data['expire']
            poster.salary       = form.cleaned_data['salary']
            poster.work_hour    = form.cleaned_data['work_hour']
            poster.poster_field = form.cleaned_data['poster_field']
            poster.save()
            return HttpResponseRedirect(reverse('poster:detail' ,args=[kwargs['pk']]))
        return super().post(request, *args, **kwargs)

@login_required(login_url="/login/")
def Request(request ,pk):
    try:
        jobseeker = get_object_or_404(JobSeeker ,pk=request.user.jobseeker.pk)
    except:
        return HttpResponseRedirect(reverse('index'))
    poster = models.Poster.objects.filter(pk=pk).first()
    if jobseeker not in poster.jobseeker.all():
        poster.jobseeker.add(jobseeker)
    return HttpResponseRedirect(reverse('poster:detail' ,args=[poster.pk]))
    