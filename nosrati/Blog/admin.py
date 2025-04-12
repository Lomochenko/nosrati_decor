from django.contrib import admin
from django.http import HttpRequest
from django_summernote.admin import SummernoteModelAdmin

from .forms import ArticleDetailInlineForm
from .models import Article, ArticleDetail


class ItemInline(admin.StackedInline):
    model = ArticleDetail
    form = ArticleDetailInlineForm
    extra = 1


@admin.register(Article)
class ProductAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'slug', 'author']
    inlines = [ItemInline]
    summernote_fields = ('article_detail_set.content',)

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)
