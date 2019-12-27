from django.db import models
from django.contrib.auth.models import User

import os

def profilePathUpload(instance, filename):
    fullFilename = "profile-" + instance.jobseeker.user.username + "-" + filename
    folderName = instance.jobseeker.user.username
    path = os.path.join('Job Seeker', folderName)
    return os.path.join(path, fullFilename)

def resumePathUpload(instance, filename):
    fullFilename = "resume-" + instance.jobseeker.user.username + "-" + filename
    folderName = instance.jobseeker.user.username
    path = os.path.join('Job Seeker', folderName)
    return os.path.join(path, fullFilename)

class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

class JobSeekerProfile(models.Model):
    jobseeker    = models.OneToOneField(JobSeeker, on_delete=models.CASCADE)
    photo        = models.ImageField(upload_to=profilePathUpload ,null=True ,blank=True)
    firstName    = models.CharField(max_length=100)
    lastName     = models.CharField(max_length=100)
    GENDER       = (
                    ('male'  , 'Male'),
                    ('female', 'Female'),
                )
    gender       = models.CharField(max_length=6 ,choices=GENDER)
    age          = models.IntegerField()
    phoneNumber = models.CharField(max_length=50 ,null=True ,blank=True)
    GRADE_CHOICE = (
                        ('Diploma' ,'Diploma'),
                        ('Bachelor', 'Bachelor'),
                        ('Master', 'Master'),
                        ('PhD', 'PhD'),
                )
    grade        = models.CharField( max_length=8 ,choices=GRADE_CHOICE)
    resume       = models.FileField(upload_to=resumePathUpload , max_length=100 ,blank=True ,null=True)
    JOB_FIELD = (
        ('software_developer' ,'Software Developer'),
        ('backend_developer'  ,'Backend Developer'),
        ('frontend_developer' ,'Frontend Developer'),
        ('civil'              ,'Civil Engineer'),
        ('mechanic'           ,'Mechanic Engineer'),
    )
    jobSeekField = models.CharField(max_length=50 ,choices=JOB_FIELD) 

    def __str__(self):
        return "Profile " + str(self.jobseeker)

class ExecutiveRecord(models.Model):
    jobseekerProfile = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)

    post  = models.CharField(max_length=300)
    start = models.CharField(max_length=30)
    end   = models.CharField(max_length=30)
    place = models.CharField(max_length=300)
    city  = models.CharField(max_length=300)

    def __str__(self):
        return str(self.jobseekerProfile.jobseeker) + " - " + self.post

class Skill(models.Model):
    jobSeekerProfile = models.ForeignKey(JobSeekerProfile ,on_delete=models.CASCADE)
    SKILL_TITLE = (
        ('c'      , 'C'),
        ('cpp'    , 'C++'),
        ('c#'     , 'C#'),
        ('java'   , 'Java'),
        ('python' , 'Python'),
        ('django' , 'Django'),
        ('office' , 'Office'),
        ('git'    , 'Git'),
        ('autocad', 'AutoCad'),
        ('solidworks', 'SolidWorks'),
        ('3dsmax', '3Ds Max'),
    )
    title = models.CharField(max_length=50 ,choices=SKILL_TITLE)
    SKILL_LEVEL = (
        ('begginer'     , 'مبتدی'),
        ('intermediate' , 'متوسط'),
        ('professional' , 'حرفه ای'),
    )
    level = models.CharField(max_length=50 ,choices=SKILL_LEVEL)

    def __str__(self):
        return str(self.jobSeekerProfile.jobseeker) + " - " + self.title