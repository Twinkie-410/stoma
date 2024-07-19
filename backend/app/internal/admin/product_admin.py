from app.internal.models.product_model import Product
from django.contrib import admin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__")
