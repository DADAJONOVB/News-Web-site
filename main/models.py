from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images')
    body = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
