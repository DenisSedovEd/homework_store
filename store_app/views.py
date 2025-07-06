from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import ProductModelForm
from .models import Product


def index(request):
    return render(request, "store_app/index.html")


def product_list(request):
    products = Product.objects.all()
    context = {
        "title": "Product List",
        "products": products,
    }
    return render(request, "store_app/product_list.html", context=context)


def add_product(request):
    if request.method == "POST":
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductModelForm()

    context = {
        "title": "Add Product",
        "form": form,
    }

    return render(request, "store_app/add_product.html", context=context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "title": "Product Detail",
        "product": product,
    }
    return render(request, "store_app/product_detail.html", context=context)


def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail", product_id=product_id)
    else:
        form = ProductModelForm(instance=product)
    context = {
        "title": "Edit Product",
        "form": form,
    }
    return render(request, "store_app/product_edit.html", context=context)
