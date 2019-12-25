from django.db import models
from django.contrib.auth.models import User

import os

def pathUpload(instance, filename):
    full_filename = "profile-" + instance.company.user.username + "-" + filename
    folder_name = instance.company.user.username
    path = os.path.join('Company', folder_name)
    return os.path.join(path, full_filename)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

class CompanyProfile(models.Model):
    company     = models.OneToOneField(Company ,on_delete=models.CASCADE)
    photo       = models.ImageField(upload_to=pathUpload ,null=True ,blank=True)
    name        = models.CharField(max_length=300)
    address     = models.TextField()
    phoneNumber = models.CharField(max_length=11)
    job_field   = models.CharField(max_length=100 ,null=True ,blank=True)
    website     = models.CharField(max_length=100 ,null=True ,blank=True)
    dateOfFoundation = models.CharField(max_length=4)

    def __str__(self):
        return "Profile " + str(self.company)