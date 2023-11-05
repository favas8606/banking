from django.db import models


# Create your models here.
class Transaction(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)
    acnumber = models.CharField(max_length=20)
    ifsc = models.TextField(max_length=10)
    date = models.DateField()
    amount = models.CharField(max_length=20)

    def __str__(self):
        return self.fname
    

class Register(models.Model):
    fname = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    lname = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=20)
    district = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.CharField(max_length=20)
    bankname = models.CharField(max_length=100,default='')
    acnumber = models.CharField(max_length=100,default='')
    ifsc = models.TextField(max_length=10, default='')
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email =  models.CharField(max_length=30)
    type_ac = models.CharField(max_length=30)
    details = models.CharField(max_length=30)

    def __str__(self):
        return self.fname


