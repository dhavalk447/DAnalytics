from django.db import models
from django.contrib.auth.models import User

# MobileType model to represent mobile brands (e.g., Apple, Samsung)
class MobileType(models.Model):
    brand = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.brand


# Mobile model to represent individual mobile phones
class Mobile(models.Model):
    company = models.ForeignKey(MobileType, related_name='mobiles', on_delete=models.CASCADE)
    mobile_name = models.CharField(max_length=100, unique=True)
    mobile_price = models.DecimalField(max_digits=10, decimal_places=2)
    storage = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.company.brand} {self.mobile_name}"


# Buyer model extending Django's User model
class Buyer(User):
    AREA_CHOICES = [
        ('W', 'Windsor'),
        ('LS', 'LaSalle'),
        ('A', 'Amherstburg'),
        ('L', 'Lakeshore'),
        ('LE', 'Leamington'),
    ]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    area = models.CharField(max_length=2, choices=AREA_CHOICES, default='A')
    interested_in = models.ManyToManyField(MobileType, related_name='interested_buyers')

    def __str__(self):
        return self.username
