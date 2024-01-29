from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Product, Recipe, RecipeProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'times_cooked', 'created_at', 'updated_at')
    search_fields = ['name', 'times_cooked']
    list_filter = (
        ('created_at', DateFieldListFilter),
        ('updated_at', DateFieldListFilter)
    )


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline, ]
    list_display = ('name', 'created_at', 'updated_at',)
    search_fields = ['name', ]
    list_filter = (
        ('created_at', DateFieldListFilter),
        ('updated_at', DateFieldListFilter)
    )
