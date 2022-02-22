from django.db import models
# from phonenumber_field.modelfields import phonenumber_field
from phone_field import PhoneField
from django_countries.fields import CountryField
# Create your models here.
class Client(models.Model):
    full_name = models.CharField(max_length=200)
    country = CountryField(blank=True)
    # company_name = models.CharField(max_length=200)
    # phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    no_of_ctns_ordered = models.CharField(max_length=200)
    no_of_cbm_ordered = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    shipping_mark = models.CharField(max_length=500)
    # date_registered = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.full_name