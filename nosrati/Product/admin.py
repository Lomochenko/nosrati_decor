from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django_summernote.admin import SummernoteModelAdmin
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
class ProductAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')  # لینک اضافه شد
    readonly_fields = ['view_on_site_link']  # نمایش در فرم هم فعال شد
    inlines = [ItemInline, DescriptInline, FAQInline]
    search_fields = ('title',)
    ordering = ('parent', 'id')
    summernote_fields = ('description_detail.content',)

    def view_on_site_link(self, obj):
        if obj.slug:
            if obj.parent is None:
                # اگه دسته‌بندی والد باشه
                url = reverse('category-page', kwargs={'slug': obj.slug})
            else:
                # اگه دسته‌بندی فرزند باشه
                url = reverse('product-page', kwargs={'slug': obj.slug})
            return format_html('<a href="{}" target="_blank">مشاهده در سایت</a>', url)
        return "-"

    view_on_site_link.short_description = "نمایش در سایت"


@admin.register(Product)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    ordering = ('id',)
    search_fields = ('title',)
