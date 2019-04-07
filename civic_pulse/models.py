from django.db import models
from django.utils import timezone


# Create your models here.
class Agency(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Entry(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    agency = models.ForeignKey(Agency)

    def __str__(self):
        return self.agency.__str__() + "_" + self.created_date.strftime("%m_%d")
