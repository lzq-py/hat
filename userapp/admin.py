from django.contrib import admin
from userapp import models
# Register your models here.

admin.site.register(models.Book)
admin.site.register(models.Author)
admin.site.register(models.Press)
admin.site.register(models.AuthorDetail)