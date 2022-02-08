from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import region, Staff
from .forms import CustomUserCreationForm, CustomUserChangeForm


CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'active', 'region']
    fieldsets = (
        (('User'), {'fields': ('username', 'email','is_staff', 'region', 'password', 'active', 'first_name', 'last_name')}),
    )

admin.site.register(region)
admin.site.register(CustomUser, CustomUserAdmin)