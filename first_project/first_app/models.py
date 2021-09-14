from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    category = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url = models.URLField()
    def __str__(self):
        return self.name

class Webdate(models.Model):
    category = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    access_date = models.DateField()
    def __str__(self):
        return str(self.access_date)
