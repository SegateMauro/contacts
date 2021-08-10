from django.db import models


class Stores(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    eMail = models.EmailField(max_length=100)
    Address = models.CharField(max_length=100)
    ZipCode = models.CharField(max_length=14)
    City = models.CharField(max_length=100)

class Workers(models.Model):
    Name = models.CharField(max_length=100)
    Store = models.CharField(max_length=10)
    Sector = models.CharField(max_length=10)
    Position = models.CharField(max_length=10)
    Phone = models.CharField(max_length=15)
    eMail = models.EmailField(max_length=100)
    Address = models.CharField(max_length=100)
    ZipCode = models.CharField(max_length=14)
    City = models.CharField(max_length=100)

class Departaments(models.Model):
    Name = models.CharField(max_length=100)

class Positions(models.Model):
    Name = models.CharField(max_length=100)