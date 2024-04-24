from django.db import models


class Animal(models.Model): # == созданию табицы в sql
    name = models.CharField(max_length=30) # атрибут с типом TEXT
    age = models.IntegerField(default=1) # INTEGER

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Product(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="products_images", blank=True, null=True)
    price = models.IntegerField()
    category = models.ManyToManyField(Category,  null=True ,blank=True)