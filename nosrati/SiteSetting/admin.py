from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import FirstContent, MainDescription, Answer, ContactUs, Employee


# Register your models here.


@admin.register(MainDescription)
class ProductAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ['title']
    summernote_fields = ('content',)


admin.site.register(FirstContent)
admin.site.register(Employee)
admin.site.register(Answer)
admin.site.register(ContactUs)
