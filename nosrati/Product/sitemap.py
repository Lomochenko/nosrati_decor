from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Category, Product


class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        # فقط دسته‌بندی‌های فعال را دریافت می‌کنیم
        return Category.objects.filter(parent=None, is_active=True)

    def lastmod(self, obj):
        return obj.create_date  # فرض می‌کنیم که `create_date` فیلد مربوط به تاریخ آخرین تغییر است

    def location(self, item):
        # ساخت URL برای دسته‌بندی
        return reverse('category-page', kwargs={'slug': item.slug})


from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Category, Product


class ProductViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        # فقط دسته‌بندی‌هایی که محصول فعال دارند رو میاریم
        return Category.objects.filter(
            is_active=True,
            product_detail__is_active=True
        ).distinct()

    def location(self, item):
        # چون ویو product با slug دسته‌بندی کار میکنه
        return reverse('product-page', kwargs={'slug': item.slug})

    def lastmod(self, obj):
        return obj.create_date  # فرض می‌کنیم که `create_date` فیلد مربوط به تاریخ آخرین تغییر است
