from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Article


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        # اگر فقط مقالات فعال را می‌خواهید فیلتر کنید:
        return Article.objects.filter(is_active=True)

    def lastmod(self, obj):
        # اگر تاریخ بروزرسانی هم دارید، می‌توانید از آن استفاده کنید.
        # فرض کنید فیلد `updated_at` برای تاریخ آخرین تغییرات دارید
        return obj.updated_at if obj.updated_at else obj.updated_at

    def location(self, item):
        return reverse('articles_detail', kwargs={'slug': item.slug})
