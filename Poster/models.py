from django.db import models
from django.urls import reverse

import os

def pathUpload(instance, filename):
    fullFilename = "poster-" + instance.company.user.username + "-" + filename
    folderName = instance.company.user.username
    path = os.path.join('Poster', folderName)
    return os.path.join(path, fullFilename)


class Poster(models.Model):
    company = models.ForeignKey("Company.Company" ,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=pathUpload ,null=True ,blank=True)
    expire = models.DateField( auto_now=False, auto_now_add=False)
    salary = models.CharField( max_length=50)
    work_hour = models.IntegerField()
    POSTER_FIELD = (
        ('software_developer' ,'Software Developer'),
        ('backend_developer'  ,'Backend Developer'),
        ('frontend_developer' ,'Frontend Developer'),
        ('civil'              ,'Civil Engineer'),
        ('mechanic'           ,'Mechanic Engineer'),
    )
    poster_field = models.CharField(max_length=50 ,choices=POSTER_FIELD)
    jobseeker = models.ManyToManyField("JobSeeker.JobSeeker", )

    def __str__(self):
        return self.company.user.username+" - "+self.title
    
    def get_absolute_url(self):
        return reverse("poster:detail", kwargs={"pk": self.pk})
    