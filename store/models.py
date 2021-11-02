from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta :
        ordering = ('ordering', )
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    photo = models.ImageField(upload_to='upload/', null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=True)

    class Meta :
        ordering = ('-created', )


    def __str__(self) -> str:
        return self.name
