from django import forms
from django.urls import clear_script_prefix
from myapp.models import image


class imageForm(forms.ModelForm):
    class Meta:
        model=image
        fields='__all__'
        labels={'image':''}