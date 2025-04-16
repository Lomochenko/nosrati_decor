from django.urls import path

from .views import ArticlesListView, ArticleDetailView

urlpatterns = [
    path('blog/', ArticlesListView.as_view(), name='article_page'),
    path('blog/<slug:slug>/', ArticleDetailView.as_view(), name='articles_detail'),
]
