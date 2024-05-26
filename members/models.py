from django.db import models
from datetime import datetime
from django.db import migrations, models
# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=300)
    
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Member(models.Model):
    MemberID = models.IntegerField(null=True)
    Fullname = models.CharField(max_length=100)
    Email = models.CharField(max_length=254)  # Adjusted max_length for email
    Phone = models.CharField(max_length=20, null=True)  # Adjusted max_length for phone
    IDNumber = models.IntegerField(null=True)
    BoardRegNo = models.CharField(max_length=15, null=True)
    Designation = models.CharField(max_length=100)
    SubSpecialization = models.CharField(max_length=100)
    Workstation = models.CharField(max_length=100)
    Affiliation = models.CharField(max_length=100)
    PostalAddress = models.CharField(max_length=255)  # Adjusted max_length for postal address
    PostalCode = models.CharField(max_length=10, null=True)  # Adjusted max_length for postal code
    TownorCity = models.CharField(max_length=100)
    DateRegistration = models.DateField(blank=True, default='', null=True)
    BackupEmail = models.CharField(max_length=254)
    Approved = models.CharField(max_length=100)  # Changed ImageField to BooleanField
    Status = models.CharField(max_length=15)
    Roles = models.CharField(max_length=100)

    
    
    def __str__(self):
       return f"{self.Fullname}"
   