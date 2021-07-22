from django.db import models

# Create your models here.
class dummproduts(models.Model):
    image = models.CharField(max_length=2002)
class Productinshop(models.Model):
    Product_name = models.CharField(max_length=255)
    image = models.CharField(max_length=2000)
class Product(models.Model):
    Product_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2000)