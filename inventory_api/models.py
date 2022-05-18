from django.db import models


class Product(models.Model):
    name= models.CharField(max_length=64)
    description = models.CharField(max_length= 256)
    price = models.IntegerField()
    quantity = models.IntegerField()

class Warehouse(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=256)
    phone = models.CharField(max_length=12)
    products = models.ManyToManyField(Product, related_name="warehouse", blank=True)