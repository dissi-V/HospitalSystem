from django.db import models


# Create your models here.

class Users(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField(null=True)
    password = models.CharField(max_length=100)
    date = models.DateField(null=True)

    def __str__(self):
        return self.fullname


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=50)
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name

class Member(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Appointment(models.Model):
    name = models.CharField(max_length=50,default="disi")
    email = models.EmailField(max_length=100,default="abc@gmail.com")
    phone = models.CharField(max_length=50,default="0123456789")
    date = models.DateField(default="2020-05-22")
    department = models.CharField(max_length=100,default="Department 1")
    doctor = models.CharField(max_length=100,default="Doctor 1")
    message = models.TextField(default="Type anything")

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    

