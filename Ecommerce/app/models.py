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