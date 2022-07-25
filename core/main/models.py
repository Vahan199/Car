from audioop import reverse
from django.db import models
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models. Model):
    name = models.CharField('Category name', max_length = 30)
    def __str__(self):
        return self.name
    # def get_absolut_url(self):
    #     return reverse(category, kwargs ={'cats id':self.pk})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorias'



class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='carcategory', null=True)
    name = models.CharField('Car name', max_length=30)
    year = models.IntegerField('Car year')
    price = models.IntegerField('Car price')
    img = models.ImageField('Car image', upload_to='media')
    content = models.TextField(blank=True)
    # в отличие от оригинала добовлено две эти строки для дат.
    time_create = models.DateTimeField(auto_now_add=True, null=True) 
    time_update = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'