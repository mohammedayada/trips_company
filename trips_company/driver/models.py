from django.db import models
from django.utils.timezone import now


# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    birthday = models.DateField(default=now)

