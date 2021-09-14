from django import forms
from first_app.models import Topic,Webpage,Webdate
from django.core import validators

'''
class FormName(forms.Form):
    topic_name = forms.CharField(label="Topic Name:")
'''
class FormName(forms.ModelForm):
    topic_name = forms.CharField()
    class Meta():
        model = Topic
        fields = "__all__"

class WebpageForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Topic.objects.all())
    name = forms.CharField(label="Name: ")
    url = forms.URLField(label="URL: ")
    class Meta():
        model = Webpage
        fields = "__all__"

class WebdateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Webpage.objects.all())
    access_date = forms.DateField(label="Access Date: ", widget=forms.SelectDateWidget)
    class Meta():
        model = Webdate
        fields = "__all__"
