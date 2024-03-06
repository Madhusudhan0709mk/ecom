from django.db import models
from api.category.models import category
# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(blank=True,default=True)
    image = models.ImageField(upload_to='images',blank=True,null=True)
    category = models.ForeignKey(category,on_delete = models.SET_NULL,null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name