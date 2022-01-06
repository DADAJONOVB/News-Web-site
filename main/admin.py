from types import MethodWrapperType
from django.contrib import admin
from .models import Image, News, Category

admin.site.register(Image)
admin.site.register(News)
admin.site.register(Category)