from django.contrib import admin

from sprintercarsapp.models import Products


class ProductAdmin(admin.ModelAdmin):
    model = Products
    fields = ('name', 'image', 'description', 'specification', 'is_latest', 'is_sold')
    list_display = (
        'id', 'name', 'image', 'description', 'specification', 'is_latest', 'is_sold')
    search_fields = ('id', 'name',)


admin.site.register(Products, ProductAdmin)
