from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class landing_pageRegistrationForm(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=80)
    #phone = PhoneNumberField()
def __str__(self):
        return self.name

