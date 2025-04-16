from django.urls import path

from .views import CategoryView, ProductView

urlpatterns = [
    path('category/<str:slug>/', CategoryView.as_view(), name='category-page'),
    path('product/<str:slug>/', ProductView.as_view(), name='product-page'),
]
