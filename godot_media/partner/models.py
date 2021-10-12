from django.db import models

# Create your models here.


class Partners(models.Model):
    name = models.CharField(max_length=60)
    gst = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=60)
    agency = models.CharField(max_length=60)
