from django.contrib import admin
from core import models

# Register your models here.
 


class CategoryAdmin(admin.ModelAdmin):
    pass


#admin.site.register(models.Category,  CategoryAdmin)