from django.contrib import admin
from .models import Brand, Laptop

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']  

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'brand', 'price'] 
