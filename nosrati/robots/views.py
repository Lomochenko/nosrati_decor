# views.py

from django.http import HttpResponse
from django.contrib.sites.models import Site
from django.urls import reverse


def robots_txt_view(request):
    current_site = Site.objects.get_current()
    sitemap_url = f"https://{current_site.domain}{reverse('django.contrib.sitemaps.views.sitemap')}"

    content = f"""User-agent: *
Disallow: /admin/
Disallow: /404/
Disallow: /500/
Disallow: /static/
Disallow: /media/
Allow: /

Sitemap: {sitemap_url}
"""
    return HttpResponse(content, content_type="text/plain")
