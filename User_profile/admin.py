from django.contrib import admin
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Profile_inline(admin.StackedInline):
    model = Customer

class user_model(admin.ModelAdmin):
    model = User
    list_display = ('email','username','date_joined','last_login','is_staff','is_superuser')
    search_fields = ('email','username')
    fieldsets = (
        ('User settings', {'fields': ('email', 'username')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Groups', {'fields': ('groups',)}),
    )       
    inlines = [Profile_inline]
    
admin.site.unregister(User)
admin.site.register(User,user_model)