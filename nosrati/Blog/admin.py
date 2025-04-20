from django.contrib import admin
from django.http import HttpRequest
from django.urls import reverse
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from .forms import ArticleDetailInlineForm
from .models import Article, ArticleDetail, ProductRecommendation, ArticleBanner


class ItemInline(admin.StackedInline):
    model = ArticleDetail
    form = ArticleDetailInlineForm
    extra = 1


class BannerInline(admin.StackedInline):
    model = ArticleBanner
    extra = 1


class ProductRecommendationInline(admin.StackedInline):
    model = ProductRecommendation
    extra = 2
    fk_name = 'primary'


@admin.register(Article)
class ProductAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'slug', 'author']
    inlines = [ItemInline, ProductRecommendationInline, BannerInline]
    readonly_fields = ['view_on_site_link']  # نمایش در فرم هم فعال شد
    summernote_fields = ('article_detail_set.content',)

    def view_on_site_link(self, obj):
        if obj.slug:
            # اگه دسته‌بندی فرزند باشه
            url = reverse('articles_detail', kwargs={'slug': obj.slug})
            return format_html('<a href="{}" target="_blank">مشاهده در سایت</a>', url)
        return "-"

    view_on_site_link.short_description = "نمایش در سایت"

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)
