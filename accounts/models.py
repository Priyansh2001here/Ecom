from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=100)
    addr = RichTextField()

class Comment(models.Model):
    comment = models.TextField()
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    to_prod = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)