from django.contrib import admin

from . import models

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(models.CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    pass