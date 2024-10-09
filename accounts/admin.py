from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # You can modify the fields displayed in the admin here if needed
    list_display = ('username', 'email', 'phone_number', 'role')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('role',)

admin.site.register(User, CustomUserAdmin)

