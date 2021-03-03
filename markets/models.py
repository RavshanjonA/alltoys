from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    descirption = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class Market(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name='markets')
    def __str__(self):
        return self.name