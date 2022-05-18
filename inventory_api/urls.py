from django.urls import path, include
from inventory_api import views

urlpatterns = [
    #products
    path("products/", views.product_list, name="product_list"),
    path("products/new", views.product_new, name="product_new"),
    path("products/<int:product_id>/", views.product_detail, name="product_detail"),
    path("products/<int:product_id>/update", views.product_update, name="product_update"),
    path("products/<int:product_id>/delete", views.product_delete, name="product_delete"),
    # warehouse
    path("warehouse/", views.warehouse_list, name="warehouse_list"),
    path("warehouse/new", views.warehouse_new, name="warehouse_new"),
    path("warehouse/<int:warehouse_id>/", views.warehouse_detail, name="warehouse_detail"),
    path("warehouse/<int:warehouse_id>/update", views.warehouse_update, name="warehouse_update"),
    path("warehouse/<int:warehouse_id>/delete", views.warehouse_delete, name="warehouse_delete"),
]
