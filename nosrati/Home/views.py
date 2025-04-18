from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from Blog.models import Article
from Home.forms import AdvertisingForm
from Product.models import Product, Category
from SiteSetting.models import ContactUs, FirstContent, MainDescription, Answer, Employee


# Create your views here.

class HomeView(TemplateView):
    template_name = 'Home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['firstContent'] = FirstContent.objects.filter(is_active=True).first()
        context['mains'] = MainDescription.objects.filter(is_active=True).order_by('-id')
        context['products'] = Product.objects.select_related('category').filter(is_first=True, is_active=True).order_by(
            '-id')[:12]
        context['categories'] = Category.objects.prefetch_related('description_detail',
                                                                  'answer_detail').filter(is_active=True,
                                                                                          parent=None).values('title',
                                                                                                              'photo',
                                                                                                              'slug')
        context['articles'] = Article.objects.filter(is_active=True).order_by('-create_date')[:3]
        context['answers'] = Answer.objects.filter(is_active=True).order_by('-id')
        return context


def site_header_component(request):
    context = {
        'categories': Category.objects.prefetch_related('description_detail', 'answer_detail').filter(is_active=True,
                                                                                                      parent=None).values(
            'title', 'slug'),
        'first': FirstContent.objects.filter(is_active=True).first(),
    }
    return render(request, 'component/site_header_component.html', context)


def site_footer_component(request):
    contact_us = ContactUs.objects.filter(is_active=True).first()
    first_category_slug = Category.objects.filter(is_active=True, parent=None).only('slug').first()
    first_content = FirstContent.objects.filter(is_active=True).first()

    # اگر هر کدوم از مقادیر None بود، مقدار پیش فرض قرار بدید
    context = {
        'contactUs': contact_us if contact_us else 'محتوای مورد نظر یافت نشد',
        'first_category_slug': first_category_slug.slug if first_category_slug else 'slug پیش‌فرض',
        'first': first_content if first_content else 'محتوای پیش‌فرض'
    }

    return render(request, 'component/site_footer_component.html', context)


def Contact_us(request):
    if request.method == 'POST':
        form = AdvertisingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('Full_Name')
            phone = form.cleaned_data.get('phone')
            text = form.cleaned_data.get('text')
            subject = form.cleaned_data.get('service_type')
            send_mail(
                'آگهی جدید',
                f'{name}\n{phone}\n{text}\n{subject}',
                'ali.naseri3179@gmail.com',
                ['hmtymslm50@gmail.com'],
                fail_silently=False,
            )
            return redirect(reverse('home-page'))
    else:
        form = AdvertisingForm()

    return render(request, 'Home/contact.html', context={'form': form})


class AboutView(TemplateView):
    template_name = 'Home/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)

        context['answers'] = Answer.objects.filter(is_active=True)
        context['employees'] = Employee.objects.filter(is_active=True)
        return context
