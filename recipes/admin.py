from django.contrib import admin
from .models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'preparation_time',
        'servings',
        'created_at',
        'is_published',
        'category',
        'author',
    ]

    list_display_links = [
        'title',
    ]

    list_editable = [
        'preparation_time',
        'servings',
        'is_published',
        'category',
        'author',
    ]
