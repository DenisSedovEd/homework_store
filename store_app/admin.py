from django.contrib import admin
from .models import Product, Status

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "status",
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

    @admin.action(description=f"Скидка на товар 20 процентов")
    def sales(self, request, queryset):
        for product in queryset:
            product.price = product.price * 0.80
            product.save()

    actions = [sales]
