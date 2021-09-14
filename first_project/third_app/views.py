from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from third_app.models import country
# Create your views here.
def index(request):
    web_list = country.objects.order_by('name')
    #my_dict = {'access_records':web_list}
    #return render(request,"third_app/index.html",context=my_dict)
    form = forms.CountryName()
    if request.method =='POST':
        form = forms.CountryName(request.POST)
        if form.is_valid():
            print("From validation is successfull, print in console.")
            print("Country Name: "+form.cleaned_data['name'])
            print("currency: "+form.cleaned_data['currency'])
            print("Bank: "+form.cleaned_data['bank'])
            form.save(commit=True)
    return render(request,'third_app/index.html', {'form':form,'access_records':web_list})
