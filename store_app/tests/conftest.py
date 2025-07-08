import pytest

from store_app.models import Product, Category, Status


@pytest.fixture
def status():
    return Status.objects.create(
        name="Some status",
    )


@pytest.fixture
def category():
    return Category.objects.create(
        name="Test Category name",
        description="Test Category description",
    )


@pytest.fixture
def product(category, status):
    return Product.objects.create(
        name="Some product",
        description="Description for some product",
        price=1000.0,
        status=status,
        category=category,
    )
