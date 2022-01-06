from types import MethodWrapperType
from django.contrib import admin
from .models import Image, News

admin.site.register(Image)
admin.site.register(News)