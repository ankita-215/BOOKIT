from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group, User
from django.utils.translation import ugettext_lazy as _, pgettext_lazy as _c
import re
from datetime import datetime,date


# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class scat(models.Model):
    sc = models.ForeignKey(Cat, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class C(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class P(models.Model):
    c = models.ForeignKey(C, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


#vehicle model
class vehicle(models.Model):
    vid = models.AutoField(primary_key=True)
    o_name = models.CharField(max_length=50)
    email=models.EmailField(max_length=60,default="")
    address= models.CharField(max_length=500, default="")
    Mono= models.CharField(max_length=13, default="")
    city= models.CharField(max_length=20,default="")
    Pincode= models.CharField(max_length=6, default="")  
    v_num = models.CharField(max_length=300,unique=True)
    category = models.ForeignKey(Cat, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(scat, on_delete=models.SET_NULL, null=True)
    status=models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")
    bstatus=models.IntegerField(default=0)
    document = models.FileField(upload_to='documents/',default="")
    adharcard=models.FileField(upload_to='documents/',default="")
    policeverification=models.FileField(upload_to='documents/',default="")
    price=models.IntegerField(default=1)
    ex=models.IntegerField(default=1)
    def __str__(self):
        return self.o_name
#user registration module
class register(models.Model):
   id = models.AutoField(primary_key=True)
   name= models.CharField(max_length=20,default="")
   address= models.CharField(max_length=500, default="")
   Mono= models.CharField(max_length=13, default="")
   city= models.CharField(max_length=20,default="")
   Pincode= models.CharField(max_length=6, default="")   
   email= models.EmailField(max_length=60,unique=True,default="")
   password= models.CharField(max_length=30)
   status=models.IntegerField(default=0)
   Rdate=models.DateField(default=date.today(), blank=True,null=True)
   def __str__(self):
        return self.name
   
#driver registration module
class driver(models.Model):
    did = models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=30,default="")
    lastname=models.CharField(max_length=30,default="")
    password=models.CharField(max_length=12,default="")
    email= models.EmailField(max_length=60,unique=True,default="")
    Mono= models.CharField(max_length=13, default="")
    city= models.CharField(max_length=20, default="")
    licence= models.FileField(upload_to='documents/',default="")
    adharcard=models.FileField(upload_to='documents/',default="")
    policeverification=models.FileField(upload_to='documents/',default="")
    mediclereport=models.FileField(upload_to='documents/',default="")
    passbook=models.FileField(upload_to='documents/',default="")
    image = models.ImageField(upload_to='shop/images', default="")
    status=models.IntegerField(default=0)
    bstatus=models.IntegerField(default=0)
    def __str__(self):
        return self.firstname + " " + self.lastname

class admin1(models.Model):
    aid = models.AutoField(primary_key=True)
    password=models.CharField(max_length=12,default="")
    email= models.EmailField(max_length=60,unique=True,default="")
    status=models.IntegerField(default=0)
    def __str__(self):
        return self.email

class book(models.Model):
    bid = models.AutoField(primary_key=True)
    name= models.CharField(max_length=20,default="")
    address= models.CharField(max_length=500, default="")
    Mono= models.CharField(max_length=13, default="")
    city = models.ForeignKey(C, on_delete=models.SET_NULL, null=True)
    p = models.ForeignKey(P, on_delete=models.SET_NULL, null=True)
    email= models.EmailField(max_length=60,default="")
    Pincode= models.CharField(max_length=6, default="")   
    v_num = models.CharField(max_length=300)
    startdate=models.DateTimeField(default=datetime.now, blank=True,null=True)
    enddate=models.DateTimeField(default=datetime.now, blank=True,null=True)
    amount=models.IntegerField(default=1)
    
    def __str__(self):
        return self.name

class dbook(models.Model):
    db = models.AutoField(primary_key=True)
    name= models.CharField(max_length=20,default="")
    address= models.CharField(max_length=500, default="")
    Mono= models.CharField(max_length=13, default="")
    city = models.ForeignKey(C, on_delete=models.SET_NULL, null=True)
    p = models.ForeignKey(P, on_delete=models.SET_NULL, null=True)
    email= models.EmailField(max_length=60,default="")
    Pincode= models.CharField(max_length=6, default="")   
    did = models.ForeignKey(driver, on_delete=models.SET_NULL, null=True)
    startdate=models.DateTimeField(default=datetime.now, blank=True,null=True)
    enddate=models.DateTimeField(default=datetime.now, blank=True,null=True)
    amount=models.IntegerField(default=1)
    def __str__(self):
        return self.name

