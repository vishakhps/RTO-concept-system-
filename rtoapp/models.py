from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class UserDetails(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=13, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    vehile_number = models.CharField(max_length=50,null=True)
    registration_number = models.CharField(max_length=50,null=True)
    registration_expiry = models.DateField(auto_now=False, null= True)
    insurance_number = models.CharField(max_length=50,null=True)
    insurance_expiry = models.DateField(auto_now=False, null= True)
    pollution_number = models.CharField(max_length=50,null=True)
    pollution_expiry = models.DateField(auto_now=False, null= True)
   
    @property
    def get_Pollution_status(self):
        
        pollution_status = ''
        if self.pollution_expiry < date.today():
            pollution_status = "Expired"
        else:
            pollution_status = "Valid"
        
        return pollution_status 

    @property
    def get_insurance_status(self):
        
        insurance_status = ''
        if self.insurance_expiry < date.today():
            insurance_status = "Expired"
        else:
            insurance_status = "Valid"
        
        return insurance_status 

    @property
    def get_registration_status(self):

        registration_status = ''
        if self.registration_expiry < date.today():
            registration_status = "Expired"
        else:
            registration_status = "Valid"
        
        return registration_status 
        
class number_plate(models.Model):
    Number_plate = models.FileField(upload_to='plate')

    class Meta:
        verbose_name = 'Number_plate'
        verbose_name_plural = 'Number_plates'

class user_nuberplate_details(models.Model):
    date = models.DateField(null=True, blank=True)
    license_number = models.CharField(max_length=25, null=True, blank=True)


