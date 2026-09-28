from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUserModel(AbstractUser):
    
    USER_TYPE = [
        ('Admin', 'Admin'),
        ('Customer', 'Customer'),
        ('Salesman', 'Salesman')
    ]
    
    image = models.ImageField(upload_to='media/user_img', null=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=20, null=True)