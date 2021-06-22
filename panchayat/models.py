from django.db import models
class Userreg(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    caste = models.CharField(max_length=30)
    religion = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    wardno = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    photo = models.FileField()
    data = models.FileField
class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    status = models.IntegerField()
class Staff(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    wardno = models.CharField(max_length=30)
    wardname = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    educationalqualification = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    photo = models.FileField()
    data=models.FileField
class Gramasabha(models.Model):
    place = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    wardno = models.CharField(max_length=30)
class Scheme(models.Model):
    scheme = models.CharField(max_length=30)
    requirements = models.CharField(max_length=30)


class Application(models.Model):
    schemeid = models.ForeignKey(Scheme,on_delete=models.CASCADE)
    userid = models.CharField(max_length=30)
    photo = models.FileField()
    residencep = models.FileField()
    idcardp = models.FileField()
    taxp = models.FileField()
    incomep = models.FileField()
    castep = models.FileField()
    status = models.IntegerField()

# Create your models here.
