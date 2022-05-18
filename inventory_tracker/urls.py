
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inventory_api/", include("inventory_api.urls"))
]
