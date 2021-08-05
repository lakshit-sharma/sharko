from django.db import models

# Create your models here.

class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=13)
    desc=models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.name

class Package(models.Model):
    city_name=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.ImageField(upload_to='home/images')

    def __str__(self):
        return self.city_name
