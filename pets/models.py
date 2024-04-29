from django.db import models


class Animal(models.Model): # == созданию табицы в sql
    title = models.CharField(max_length=30) # атрибут с типом TEXT
    slug = models.CharField(max_length=100, default='/')

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    animal = models.ManyToManyField(Animal,  null=True ,blank=True)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="products_images", blank=True, null=True)
    price = models.IntegerField()
    category = models.ManyToManyField(Category,  null=True ,blank=True)