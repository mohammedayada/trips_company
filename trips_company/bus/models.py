from django.db import models
from django.utils.timezone import now

# Create your models here.
Status_Choices = [
    ('ava', 'Available'),
    ('not', 'Not available'),
]
class Bus(models.Model):
    number = models.CharField(max_length=10)
    status = models.CharField(choices=Status_Choices, max_length=3, default='ava')
    model = models.DateField(default=now)
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.number


