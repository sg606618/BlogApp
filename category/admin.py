from django.contrib import admin

from category.models import Category, Blog


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')
    search_fields = ('category_name', )
    list_display_links = ('category_name', )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'content', 'heading')
    search_fields = ('title', )
    list_display_links = ('title', )

