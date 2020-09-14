from django.contrib import admin
from .models import *
from orders.models import Order
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'active','slug', 'price', 'category', 'date_updated']
    prepopulated_fields = {'slug': ('name',)}

    list_filter = ['active', 'category']
    list_editable = ['price', 'active']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ['date_updated', 'paid', 'second_name']

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_filter = ['active', 'date_added']

@admin.register(GalleryPicture)
class GalleryPictureAdmin(admin.ModelAdmin):
    list_filter = ['date_added', 'gallery_item']

@admin.register(DeliveryOption)
class DeliveryOptionAdmin(admin.ModelAdmin):
    list_filter = ['name']

