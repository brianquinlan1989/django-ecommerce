from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.

class Review(models.Model):
      
        
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name='posts', null=False, on_delete=models.PROTECT)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, related_name='reviews', null=False, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title
