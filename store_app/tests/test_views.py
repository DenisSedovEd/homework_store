import pytest

from django.urls import reverse

from store_app.models import Product


@pytest.mark.django_db
def test_product_detail_view(client, product):
    url = reverse("product_detail", kwargs={"pk": product.id})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context_data["product"].id == product.id
    assert response.context_data["product"].name == product.name
    assert response.context_data["product"].description == product.description


@pytest.mark.django_db
def test_product_delete_view(client, product):
    url = reverse(
        "product_delete",
        kwargs={"pk": product.id},
    )
    response = client.get(url)
    assert response.status_code == 200
    assert response.context_data["product"].id == product.id

    response = client.post(url)
    assert response.status_code == 302
    assert not Product.objects.filter(id=product.id).exists()


@pytest.mark.django_db
def test_product_edit_view(client, product, category, status):
    url = reverse(
        "product_edit",
        kwargs={"pk": product.id},
    )
    response = client.get(url)
    assert response.status_code == 200
    assert "form" in response.context
    assert response.context["form"].instance == product

    edited_data = {
        "name": "New product name",
        "description": "New product description",
        "price": 999.99,
        "category": category.id,
        "status": status.id,
    }

    response = client.post(url, data=edited_data)
    assert response.status_code == 302
    assert response.url == reverse("product_list")

    product.refresh_from_db()
    assert product.name == edited_data["name"]
    assert product.description == edited_data["description"]
    assert product.price == edited_data["price"]
    assert product.category.id == edited_data["category"]
    assert product.status.id == edited_data["status"]


@pytest.mark.django_db
def test_product_list_view(client, product):
    url = reverse("product_list")
    response = client.get(url)
    assert response.status_code == 200
