from django.forms import ModelForm
from inventory_api.models import Product, Warehouse


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "quantity" ]

class WarehouseForm(ModelForm):
    class Meta:
        model = Warehouse
        fields = ["name", "location", "phone", "products"]