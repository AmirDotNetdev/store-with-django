from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    user = models.OneToOneField(User ,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    desc = models.TextField(max_length=150,blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_Id = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE)
    dateCreated = models.DateField(auto_now_add=True)
    transaction_Id = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(blank=True,null=True)

class ShippingAddress(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    city = models.TextField()
    street = models.TextField()
    zipcode = models.IntegerField()