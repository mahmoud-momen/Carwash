from django.db import models
from django.utils import timezone


class Reservation(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    SERVICE_CHOICES = (
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Complex', 'Complex'),
    )
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    car_model = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()


