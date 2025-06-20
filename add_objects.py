import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from store_app.models import Product, Category


def add_categories(categories):
    res = []
    for category in categories:
        add_obj = Category(name=category["name"], description=category["description"])
        add_obj.save()
        res.append(add_obj)
    return res


def add_products(products):
    res = []
    for product in products:
        category = Category.objects.get(name=product["category"])
        Product.objects.create(
            name=product["name"],
            description=product["description"],
            price=product["price"],
            category=category,
        )
        res.append(product)
    return res


def main():

    categories = [
        {
            "name": "Technique",
            "description": "Technique",
        },
        {
            "name": "Clothes",
            "description": "Clothes",
        },
        {
            "name": "Shoes",
            "description": "Shoes",
        },
    ]
    created_categories = add_categories(categories)
    print(created_categories)

    products = [
        {
            "name": "Телефон",
            "description": "Дешевый телефон",
            "price": 10000,
            "category": "Technique",
        },
        {
            "name": "Штаны",
            "description": "Серые штаны",
            "price": 1000,
            "category": "Clothes",
        },
        {
            "name": "Сланцы",
            "description": "Сланцы ходить на пляж",
            "price": 500,
            "category": "Shoes",
        },
    ]
    created_products = add_products(products)
    print(created_products)


if __name__ == "__main__":
    main()
