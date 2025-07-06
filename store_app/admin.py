from django.contrib import admin
from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "price",
    ]
    list_filter = [
        "category",
        "price",
    ]
    search_fields = [
        "name",
        "category",
    ]
