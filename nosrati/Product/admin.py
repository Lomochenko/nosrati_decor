from django.contrib import admin

from .forms import DesciptionForm
from .models import Product, Category, Desciption, AnswerCategory


class ItemInline(admin.StackedInline):
    model = Product
    extra = 1
    autocomplete_fields = ('category',)


class DescriptInline(admin.StackedInline):
    model = Desciption
    extra = 1
    form = DesciptionForm
    autocomplete_fields = ('category',)


class FAQInline(admin.StackedInline):
    model = AnswerCategory
    extra = 1
    autocomplete_fields = ('category',)


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')
    inlines = [ItemInline, DescriptInline, FAQInline]
    search_fields = ('title',)
    ordering = ('parent', 'id')
    summernote_fields = ('description_detail.content',)


@admin.register(Product)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    ordering = ('id',)
    search_fields = ('title',)
