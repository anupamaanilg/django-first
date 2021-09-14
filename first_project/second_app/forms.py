from django import forms
from second_app.models import vehicle,car,bike
from django.core import validators

class VehicleName(forms.ModelForm):
    company = forms.CharField()
    class Meta():
        model = vehicle
        fields = "__all__"
class CarForm(forms.ModelForm):
    c_name = forms.ModelChoiceField(queryset=vehicle.objects.all())
    model = forms.CharField(label="Model")
    class Meta():
        model = car
        fields = "__all__"
class BikeForm(forms.ModelForm):
    b_name = forms.ModelChoiceField(queryset=car.objects.all())
    price = forms.IntegerField()
    class Meta():
        model = bike
        fields = "__all__"
