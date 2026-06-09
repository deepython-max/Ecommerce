from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  #this will displayed in django admin and while selecting category in product
        return self.name
# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100,unique=True)
    # mobile= models.IntegerField(unique=True)
    mobile = models.CharField(max_length=10)
    # email= models.EmailField(unique=True)
    email= models.EmailField(unique=True)
    password= models.CharField(max_length=50)

    def __str__(self):
        return self.name\
        

    
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='product_image')
    brand=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    

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
    
class Cart(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name

class Cheakout(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    conmpany_name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()   
    notes=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    

class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    email= models.EmailField()
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    review = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return f"{self.name} - {self.product.name}"