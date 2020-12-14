from django.db import models

# Create your models here.

class Brand(models.Model):
    name=models.CharField(max_length=80,default="local")
    def __str__(self):
        return self.name

class Laptop(models.Model):
    #name
    name=models.CharField(max_length=80,default="null")
    #for processor
    cpu=models.CharField(max_length=80,default="null")
    chipset=models.CharField(max_length=80,default="null")
    gpu=models.CharField(max_length=80,default="null")
    #for Display
    technology=models.CharField(max_length=80,default="null")
    size=models.CharField(max_length=80,default="null")
    resolution=models.CharField(max_length=80,default="null")
    #for memory
    ram=models.CharField(max_length=80,default="null")
    hardDisk=models.CharField(max_length=80,default="null")
    #for connectivity
    WLAN=models.CharField(max_length=80,default="null")
    BlueTooth=models.CharField(max_length=80,default="null")
    GPS=models.CharField(max_length=80,default="null")
    Radio=models.CharField(max_length=80,default="null")
    #Other Features
    sensors=models.CharField(max_length=80,default="null")
    audio=models.CharField(max_length=80,default="null")
    browser=models.CharField(max_length=80,default="null")
    messaging=models.CharField(max_length=80,default="null")
    games=models.CharField(max_length=80,default="null")
    #for battery
    capacity=models.CharField(max_length=80,default="null")
    fastCharging=models.CharField(max_length=80,default="null")
    #price
    price=models.IntegerField(default=0)
    #rating
    ratingStars=models.FloatField(default=0)
    #reviews
    noOfReviews=models.IntegerField(default=0)
    #image Field
    image=models.ImageField(upload_to="shopApp/images",default="")
    #Description
    desc=models.CharField(max_length=2500,default="Description....")
    #brand(It is a foreign key)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return (self.name[:30]+"....")


