from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import MainDescription


class PostForm(forms.ModelForm):
    class Meta:
        model = MainDescription
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
        }
