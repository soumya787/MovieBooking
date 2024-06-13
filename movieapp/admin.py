from django.contrib import admin
from movieapp import models
# Register your models here.
admin.site.register(models.Heroes)
admin.site.register(models.Heroines)
admin.site.register(models.Director)
admin.site.register(models.Theater)