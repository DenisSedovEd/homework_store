from django.urls import path
from store_app import views

urlpatterns = [
    path("", views.IndexTemplateView.as_view(), name="index"),
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path("products/add/", views.ProductCreateView.as_view(), name="add_product"),
    path(
        "product/<int:pk>",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "product/<int:pk>/edit/",
        views.ProductUpdateView.as_view(),
        name="product_edit",
    ),
    path(
        "product/<int:pk>/delete/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
]
