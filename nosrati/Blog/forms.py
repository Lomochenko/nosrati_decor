from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import ArticleDetail


class ArticleDetailInlineForm(forms.ModelForm):
    class Meta:
        model = ArticleDetail
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
        }
