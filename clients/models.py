from django.db import models
# from phonenumber_field.modelfields import phonenumber_field
from phone_field import PhoneField
# Create your models here.
class Client(models.Model):
    full_name = models.CharField(max_length=200)
    # phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    