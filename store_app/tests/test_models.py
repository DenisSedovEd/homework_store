import pytest

from store_app.models import Product, Category, Status


@pytest.mark.django_db
def test_category_create(category):
    assert Category.objects.count() == 1
    assert category.name == "Test Category name"
    assert category.description == "Test Category description"


@pytest.mark.django_db
def test_status_create(status):
    assert Status.objects.count() == 1
    assert status.name == "Some status"


@pytest.mark.django_db
def test_product_create(product, category):
    assert Product.objects.count() == 1
    assert product.name == "Some product"
    assert product.description == "Description for some product"
    assert product.price == 1000.0
