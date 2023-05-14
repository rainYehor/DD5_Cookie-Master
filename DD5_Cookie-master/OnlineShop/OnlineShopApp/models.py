from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    price = models.IntegerField()