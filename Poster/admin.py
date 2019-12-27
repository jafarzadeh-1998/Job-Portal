from django.contrib import admin

from . import models
# Register your models here.
@admin.register(models.Poster)
class PosterAdmin(admin.ModelAdmin):
    pass