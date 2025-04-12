from django.contrib import admin

from .models import FirstContent, MainDescription, Answer, ContactUs

# Register your models here.


admin.site.register(FirstContent)
admin.site.register(MainDescription)
admin.site.register(Answer)
admin.site.register(ContactUs)
