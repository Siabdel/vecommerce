from django.contrib import admin
from store import models

# Register your models here.
 


class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Category,  CategoryAdmin)
admin.site.register(models.Product,  ProductAdmin)