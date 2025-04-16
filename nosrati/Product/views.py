from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from .models import Category, Product


# Create your views here.


class CategoryView(TemplateView):
    template_name = 'Product/category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        category_name = self.kwargs.get('slug')
        category = Category.objects.filter(slug=category_name, is_active=True).first()
        if not category:
            raise Http404()
        parent_categories = list(
            Category.objects.filter(parent=None, is_active=True)
            .order_by('id')
            .values('id', 'title', 'slug', 'photo')
        )

        # پیدا کردن ایندکس دسته‌ی فعلی
        current_index = next((i for i, c in enumerate(parent_categories) if c['id'] == category.id), None)

        # گرفتن دسته‌ی بعدی
        if current_index is not None and current_index + 1 < len(parent_categories):
            next_category = parent_categories[current_index + 1]
        else:
            next_category = parent_categories[0] if parent_categories else None

        context['next_category'] = next_category
        context['category'] = category

        return context


class ProductView(ListView):
    model = Product
    template_name = 'Product/product.html'
    context_object_name = 'products'
    ordering = ('-id',)
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super(ProductView, self).get_context_data(*args, **kwargs)
        category_name = self.kwargs.get('slug')
        category = Category.objects.filter(is_active=True, slug=category_name).first()
        if not category:
            raise Http404()
        context['category'] = category

        parent_categories = list(
            Category.objects.filter(parent=category.parent, is_active=True)
            .order_by('id')
            .values('id', 'title', 'slug', 'photo')
        )

        context['breadcrumbs'] = [
            {'title': 'خانه', 'url': reverse('home-page')},
            {'title': 'دسته‌بندی‌ها', 'url': reverse('category-page', kwargs={'slug': category.parent.slug})},
            {'title': category.title, 'url': None}  # Current category is the last item in breadcrumb
        ]

        # پیدا کردن ایندکس دسته‌ی فعلی
        current_index = next((i for i, c in enumerate(parent_categories) if c['id'] == category.id), None)

        # گرفتن دسته‌ی بعدی
        if current_index is not None and current_index + 1 < len(parent_categories):
            next_category = parent_categories[current_index + 1]
        else:
            next_category = parent_categories[0] if parent_categories else None

        context['next_category'] = next_category

        siblings = Category.objects.filter(
            parent=category.parent
        ).exclude(id=category.id).values('title', 'slug')
        context['siblings'] = siblings
        return context

    def get_queryset(self):
        query = super(ProductView, self).get_queryset()
        query = query.filter(is_active=True).select_related('category').values('title', 'content', 'photo')
        category_name = self.kwargs.get('slug')
        if category_name is not None:
            query = query.filter(category__slug=category_name)
        return query
