from django.db import models

# Create your models here.
class vehicle(models.Model):
    company = models.CharField(max_length=250,unique=True)
    #name = models.CharField(max_length=250)

    def __str__(self):
        return self.company

class car(models.Model):
    c_name= models.ForeignKey(vehicle,on_delete=models.CASCADE)
    model = models.CharField(max_length=250)
    def __str__(self):
        return self.model

class bike(models.Model):
    b_name = models.ForeignKey(car,on_delete=models.CASCADE)
    price = models.IntegerField()
    def __str__(self):
        return str(self.b_name)
