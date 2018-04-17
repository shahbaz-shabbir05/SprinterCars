from django.contrib import admin

from sprintercarsapp.models import Products, SliderImages, Testimonial


class ProductAdmin(admin.ModelAdmin):
    model = Products
    fields = ('name', 'image', 'description', 'specification', 'is_latest', 'is_sold')
    list_display = (
        'id', 'name', 'image', 'description', 'specification', 'is_latest', 'is_sold')
    search_fields = ('id', 'name',)


class SliderImageAdmin(admin.ModelAdmin):
    model = Products
    fields = ('slider_image',)
    list_display = ('id', 'slider_image',)


admin.site.register(Products, ProductAdmin)
admin.site.register(SliderImages, SliderImageAdmin)
admin.site.register(Testimonial)
