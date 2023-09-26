from django.contrib import admin

from main.models import Category, Product


# admin.site.register(Student)

@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_preview', 'category', 'purchase_price', 'date_creation', 'date_last_mod')

