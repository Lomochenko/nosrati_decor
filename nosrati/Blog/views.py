from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Article


# Create your views here.
class ArticlesListView(ListView):
    model = Article
    paginate_by = 12
    template_name = 'Blog/blogs.html'
    context_object_name = 'articles'
    ordering = ('-id',)

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        return query


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'Blog/blog_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        context['breadcrumbs'] = [
            {'title': 'خانه', 'url': reverse('home-page')},
            {'title': 'مقالات', 'url': reverse('article_page')},

        ]
        return context
