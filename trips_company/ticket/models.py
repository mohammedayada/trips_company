from django.db import models
from django.contrib.auth.models import User
from trip.models import Trip
# Create your models here.
Availability_Choices = [
    ('ava', 'Available'),
    ('not', 'Not available'),
]
class Ticket(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    availability = models.CharField(choices=Availability_Choices, max_length=3, default='ava')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    def __str__(self):
        return self.trip.name + ' ' + self.trip.price+' '+self.trip.start_date
