from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Store(models.Model):

    name = models.CharField(max_length=30)
    about = models.TextField(default="-")
    abouttxt = models.TextField(default="")
    generic = models.TextField()
    elements = models.TextField()
    facebook = models.CharField(default="-",max_length=30)
    twitter = models.CharField(default="-", max_length=30)
    dribbble = models.CharField(default="-", max_length=30)
    behance = models.CharField(default="-", max_length=30)
    tell = models.CharField(default="-", max_length=30)
    link = models.CharField(default="-", max_length=30)

    set_name = models.CharField(default="-", max_length=30)

    def __str__(self):
       return self.name + " | " + str(self.pk)



class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200, null=True)



class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=True)
    #image = models.Image(null=True,blank=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complate = models.BooleanField(default=False, null=True,blank=False)
    transaction_id = models.CharField(max_length=100,null=True)


class Orderitems(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)