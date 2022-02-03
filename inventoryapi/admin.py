from django.contrib import admin
from .models import Product, Supplier, Inventory

# Register your models here.
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Inventory)