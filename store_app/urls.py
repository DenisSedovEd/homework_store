from django.urls import path
from store_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.add_product, name="add_product"),
    path("product/<int:product_id>", views.product_detail, name="product_detail"),
    path("product/<int:product_id>/edit/", views.product_edit, name="product_edit"),
]
