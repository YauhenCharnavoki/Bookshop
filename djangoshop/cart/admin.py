from django.contrib import admin
from .models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'city', 'address')

admin.site.register(Purchase, PurchaseAdmin)