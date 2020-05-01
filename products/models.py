from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField()
    desc = RichTextField()
    seller = models.ManyToManyField('accounts.Seller')
    category = models.ManyToManyField(Category)
    price = models.IntegerField()
