from django.db import models


# Create your models here.


class FirstContent(models.Model):
    title = models.CharField(max_length=128, verbose_name='نام سایت')
    description = models.TextField(verbose_name='توضیحات اولیه')
    photo = models.ImageField(upload_to='logo/', verbose_name='لوگو')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'نام و لوگو'
        verbose_name_plural = 'نام و لوگو'


class MainDescription(models.Model):
    title = models.CharField(max_length=128, verbose_name='نام سایت')
    content = models.TextField(verbose_name='توضیحات تکمیلی')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'خدمات ما'
        verbose_name_plural = 'خدمات ما'


class Answer(models.Model):
    question = models.CharField(max_length=256, verbose_name='پرسش')
    answer = models.TextField(verbose_name='پاسخ')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'پرسش'
        verbose_name_plural = 'پرسش و پاسخ'


class ContactUs(models.Model):
    address = models.TextField(verbose_name='آدرس')
    location = models.URLField(max_length=1024, verbose_name='لینک گوگل مپ')
    phone = models.CharField(max_length=16, verbose_name='شماره')
    phone_office = models.CharField(max_length=16, verbose_name='شماره دفتر')
    instagram = models.CharField(max_length=48, verbose_name='اینستاگرام')
    whatsapp = models.URLField(max_length=256, verbose_name='لینک واتس آپ')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.instagram

    class Meta:
        verbose_name = 'راه ارتباطی'
        verbose_name_plural = 'راه ارتباطی'


class Employee(models.Model):
    title = models.CharField(max_length=48, verbose_name='نام')
    photo = models.ImageField(upload_to='about/', verbose_name='عکس', null=True, blank=True)
    job = models.CharField(max_length=48, verbose_name='سمت')
    phone = models.CharField(max_length=16, verbose_name='شماره', null=True, blank=True)
    content = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    whatsapp = models.URLField(max_length=256, verbose_name='لینک واتس آپ', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پرسنل'
        verbose_name_plural = 'پرسنل'
