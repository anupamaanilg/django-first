from django.db import models

# Create your models here.
class country(models.Model):
    name = models.CharField(max_length=250)
    currency = models.CharField(max_length=250)
    bank = models.CharField(max_length=250)
