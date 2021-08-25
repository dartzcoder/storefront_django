from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'store_price', 'inventory', 'inventory_status', 'collection_title']
    list_editable = ['store_price']
    ordering = ['inventory']
    list_per_page = 10
    #Optimizes query
    list_select_related = ['collection']
    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer_id", "customer_name"]
    list_per_page = 10
    list_select_related = ['customer']
    def customer_name(self, order):
        return f'{order.customer.first_name} {order.customer.last_name}'
    
admin.site.register(models.Collection)
admin.site.register(models.OrderItem)
