from django import forms
from third_app.models import country
from django.core import validators

class CountryName(forms.ModelForm):
    name = forms.CharField()
    currency = forms.CharField()
    bank = forms.CharField()
    class Meta():
        model = country
        fields = "__all__"
