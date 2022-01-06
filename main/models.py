from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    photo = models.ImageField(upload_to='images')

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,  null=True)
    title = models.CharField(max_length=255)
    image = models.ManyToManyField(Image)
    body = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
