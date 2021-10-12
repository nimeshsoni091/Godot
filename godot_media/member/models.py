from django.db import models
from partner.models import Partners

# Create your models here.


class Members(models.Model):
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=60)
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)
