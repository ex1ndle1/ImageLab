from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.ImageModel)
admin.site.register(models.ImageCategory)
admin.site.register(models.ImageModel)
admin.site.register(models.User)