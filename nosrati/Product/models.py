from django.db import models
from slugify import slugify


# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='دسته بندی والد')
    title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان دسته بندی')
    photo = models.ImageField(upload_to='category/', verbose_name='عکس دسته بندی', null=True, blank=True)
    url_title = models.CharField(max_length=200, unique=True, verbose_name='عنوان انگلیسی در url')
    slug = models.SlugField(verbose_name='عنوان در url', blank=True, editable=False, allow_unicode=True)
    blog = models.ForeignKey('Blog.Article',on_delete=models.CASCADE,verbose_name='مقاله های مرتبط')
    create_date = models.DateTimeField(null=True, verbose_name='تاریخ')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.url_title, allow_unicode=True, separator='_')
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی محصولات'
        verbose_name_plural = 'دسته بندی های محصولات'
        ordering = ('id',)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی',
                                 related_name='product_detail')
    title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان محصول')
    content = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    photo = models.ImageField(upload_to='products/', verbose_name='عکس محصول')
    is_first = models.BooleanField(default=False, verbose_name='نمایش در صفحه اول')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'
        ordering = ('id',)


class Desciption(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی',
                                 related_name='description_detail')
    title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان محصول')
    content = models.TextField(verbose_name='توضیحات', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'توضیحات دسته بندی'
        verbose_name_plural = 'توضیحات دسته بندی'
        ordering = ('id',)


class AnswerCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی',
                                 related_name='answer_detail')
    question = models.CharField(max_length=256, verbose_name='پرسش')
    answer = models.TextField(verbose_name='پاسخ')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'پرسش'
        verbose_name_plural = 'پرسش و پاسخ'
        ordering = ('id',)
