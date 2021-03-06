from django.db import models
from django.utils.timezone import now
from bus.models import Bus
from driver.models import Driver

# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    start_date = models.DateTimeField(default=now)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    bus = models.ManyToManyField(Bus)
    driver = models.ManyToManyField(Driver)
    def __str__(self):
        return self.name


