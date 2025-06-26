from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=50, choices=[('Vegetable', 'Vegetable'), ('Fruit', 'Fruit')])

    def __str__(self):
        return self.name
