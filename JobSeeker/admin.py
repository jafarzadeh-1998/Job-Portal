from django.contrib import admin

from . import models

@admin.register(models.JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    pass

@admin.register(models.JobSeekerProfile)
class JobSeekerProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ExecutiveRecord)
class ExecutiveRecordAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    pass