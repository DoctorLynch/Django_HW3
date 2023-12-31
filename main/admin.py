from django.contrib import admin

from main.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'purchase_price',)
    list_filter = ('category',)
    search_fields = ('name', 'description')
