from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "image", "category", "status"]
        labels = {
            "name": "Название",
            "price": "Цена",
            "description": "Описание",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название товара",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Укажите стоимость товара",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Описание товара",
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 5:
            raise ValidationError("Название товара должно быть не короче 5 символов")

    def clean_price(self):
        price = self.cleaned_data["price"]
        if not isinstance(price, int | float):
            raise ValidationError("Стоимость не может содержать нечисловые значения.")
        elif price <= 0:
            raise ValidationError("Стоимость не может быть отрицательным значением.")

    def clean_description(self):
        description = self.cleaned_data["description"]
        if "плохое слово" in description:
            raise ValidationError("Описание содержит плохое слово!!!")
