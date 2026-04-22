from django.db import models


# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100,unique=True)
    # mobile= models.IntegerField(unique=True)
    mobile= models.IntegerField()
    # email= models.EmailField(unique=True)
    email= models.EmailField(unique=True)
    password= models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='product_image')
    brand=models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    project = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name