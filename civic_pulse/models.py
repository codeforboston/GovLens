from django.db import models
from django.utils import timezone


# Create your models here.
class Agency(models.Model):
    id = models.IntegerField(primary_key=True)
    created_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=250)
    website = models.CharField(max_length=100,blank=True)
    twitter = models.CharField(max_length=100,blank=True)
    facebook = models.CharField(max_length=100,blank=True)
    phone_number = models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    agency = models.ForeignKey(Agency,on_delete=models.CASCADE)

    # Security/Privacy
    https_enabled = models.BooleanField(default=False)
    has_privacy_policy = models.BooleanField(default=False)

    # A11y
    mobile_friendly = models.BooleanField(default=False)
    good_performance = models.BooleanField(default=False)

    # Outreach/Communication
    has_social_media = models.BooleanField(default=False)
    has_contact_info = models.BooleanField(default=False)

    def __str__(self):
        return self.agency.__str__() + "_" + self.created_date.strftime("%m_%d")
