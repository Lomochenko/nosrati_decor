from django.db import models
from slugify import slugify


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    title_2 = models.CharField(max_length=300, unique=True, verbose_name='عنوان انگلیسی')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='عنوان url', editable=False)
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ثبت')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='اخرین آپدیت')
    author = models.ForeignKey("User.User", on_delete=models.CASCADE, verbose_name='نویسنده', null=True, editable=False)
    recommended_products = models.ManyToManyField('Article', through='ProductRecommendation', blank=True)
    is_active = models.BooleanField(default=False, verbose_name='نمایش در صفحه اول')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_2, allow_unicode=True, separator='_')

        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ('id',)


class ProductRecommendation(models.Model):
    primary = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='primary_recommendation')
    recommendation = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    rank = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.primary.title

    class Meta:
        verbose_name = 'محصول پیشنهادی'
        unique_together = ('primary', 'recommendation')
        ordering = ('primary', '-rank')


class ArticleDetail(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان مقاله')
    content = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله', null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله',
                                related_name='article_detail_set')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'توضیحات مقاله'
        verbose_name_plural = 'توضیحات مقالات'
