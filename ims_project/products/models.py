from django.db import models

# Create your models here.
class ProductModel(models.Model):
    
    PRODUCT_TYPE = [
        ('Fruits', 'Fruits'),
        ('Fashion', 'Fashion'),
        ('Grocery', 'Grocery'),
        ('Gadget', 'Gadget')
    ]
    
    product_name = models.CharField(max_length=100, verbose_name='Product Name', null=True)
    description = models.TextField(null=True)
    production_date = models.DateField(verbose_name='Production Date',null=True)
    image = models.ImageField(upload_to='media/product_img', null=True)
    product_type = models.CharField(choices=PRODUCT_TYPE, max_length=40, verbose_name='Product Type', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At')
    
    def __str__(self):
        return f'{self.product_name} - {self.product_type}'    
