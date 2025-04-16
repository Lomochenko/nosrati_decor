from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    # برای تعریف صفحات استاتیک
    def items(self):
        return [
            "home-page",
            "article_page",
            "contact-us",
            "about-page"
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == "home-page":
            return 1.0  # اولویت صفحه خانه بالاتر است
        elif item == "article_page":
            return 0.6  # اولویت صفحه مقالات کمی کمتر است
        return 0.5  # صفحات دیگر

    def changefreq(self, item):
        if item == "home-page":
            return "monthly"
        elif item == "article_page":
            return "weekly"
        elif item == "contact-us":
            return "yearly"
        return "never"

    def lastmod(self, item):
        # اگر می‌خواهید تاریخ آخرین تغییر صفحه را تنظیم کنید (اختیاری)
        from django.utils import timezone
        return timezone.now()
