from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=20,null=True,blank=True)
    description = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['productName','description','price']
 
    def __str__(self):
           return self.productName
