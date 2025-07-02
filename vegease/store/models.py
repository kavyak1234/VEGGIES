from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/')
    is_flash_deal = models.BooleanField(default=False)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

is_deal_of_day = models.BooleanField(default=False)

