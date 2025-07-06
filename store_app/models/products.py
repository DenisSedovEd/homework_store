from django.db import models
from .statuses import Status


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )
    image = models.ImageField(upload_to="product_images/", null=True, blank=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="products", default=1
    )

    def __str__(self):
        return f"Продукт {self.name} из категории {self.category}, цена {self.price} "
