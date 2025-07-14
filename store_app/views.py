from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)
from django.views.generic.base import TemplateView

from .forms import ProductModelForm
from .models import Product
from .tasks import send_mail_message


class IndexTemplateView(TemplateView):
    template_name = "store_app/index.html"


class ProductListView(ListView):
    model = Product
    template_name = "store_app/product_list.html"
    context_object_name = "products"


class ProductCreateView(CreateView):
    model = Product
    template_name = "store_app/add_product.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        messages.success(self.request, "Product created successfully")
        send_mail_message(
            recipient_list=["user@mail.com"],
            subject="Создана карточка товара",
            message=f'Товар: {form.cleaned_data["name"]} был добавлен в каталог.',
        )
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = "store_app/product_detail.html"
    context_object_name = "product"


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "store_app/product_edit.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "store_app/deleted_product.html"
    success_url = reverse_lazy("product_list")
