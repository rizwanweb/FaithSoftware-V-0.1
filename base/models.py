from django.db import models
import datetime

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    challanNo = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    phone1 = models.CharField(max_length=50, null=True, blank=True)
    phone2 = models.CharField(max_length=50, null=True, blank=True)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name +" - "+self.challanNo

#Item Object
class Item(models.Model):

    name = models.CharField(max_length=100)
    hscode = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


#Terminal
class Terminal(models.Model):
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.shortname


#Shipping line
class ShippingLine(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=20, null=True, blank=True)
    shortname = models.CharField(max_length=10, null=True,blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        name = self.name
        word = name.split()[0]
        self.shortname = word
        super(ShippingLine, self).save(*args, **kwargs)


#LOLO
class LOLO(models.Model):
    loloname = models.CharField(max_length=250)
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        ordering = ['loloname']
    def __str__(self):
        return self.loloname