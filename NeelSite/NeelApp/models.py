from django.db import models

# Create your models here.

class CreateNewList(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=400)
    address = models.CharField(max_length=400)

def __str__(self):
    return self.name