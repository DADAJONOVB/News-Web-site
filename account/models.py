from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey

class Staff(AbstractUser):
    region = models.ForeignKey('region', on_delete=models.SET_NULL, null=True, blank=True, related_name='staff')
    raqam = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=False)


class region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name