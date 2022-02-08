from datetime import timezone
from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class News(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='new')
    category = models.ManyToManyField(Category, blank=True)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images', blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
