from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Desciption


class DesciptionForm(forms.ModelForm):
    class Meta:
        model = Desciption
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
        }
