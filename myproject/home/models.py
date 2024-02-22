from django.db import models

# Create your models here.


class Ragister(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobilenumber = models.IntegerField()
    Dob = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    company_n = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
