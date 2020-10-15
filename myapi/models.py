from django.db import models

# Create your models here.
class EconomicData(models.Model):
    dollarBought = models.CharField(max_length=60)
    dollarSold = models.CharField(max_length=60)