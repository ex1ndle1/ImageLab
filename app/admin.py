from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.ImageModel)
admin.site.register(models.ImageCategory)


@admin.register(models.ImageModel)
class ImageAdminPanel(admin.ModelAdmin):
   list_per_page = 20    


@admin.register(models.User)
class UserAdminPanel(admin.ModelAdmin):
    list_per_page = 5