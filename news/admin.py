from django.contrib import admin
from news import models
# Register your models here.


admin.site.register(models.Reporter)
admin.site.register(models.Article)
