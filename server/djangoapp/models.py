# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.name


# Model class
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('TWO-SEAT', 'Two-seat'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon')
    ]
    car_type = models.CharField(
        max_length=10,
        choices=CAR_TYPES, default='SEDAN')
    year = models.IntegerField(
        default=2024,
        validators=[MaxValueValidator(2024),MinValueValidator(2017)])

    def __str__(self):
        return self.name

