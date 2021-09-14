from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from second_app.models import vehicle,car,bike
# Create your views here.
def index(request):
    web_list = bike.objects.order_by('price')
    web_car = car.objects.order_by('model')
    '''my_dict = {'access_records':web_list, 'access_car':web_car}
    return render(request,"second_app/index.html",context=my_dict)'''

    form = forms.VehicleName()
    #check to see if get a post back.
    if request.method =='POST':
        #in which case we pass in that request.
        formsubmitted = forms.VehicleName(request.POST)
        #check to see form is valid.
        if formsubmitted.is_valid():
            #do something
            print("From validation is successfull, print in console.")
            print("Company Name: "+formsubmitted.cleaned_data['company'])
            form.save(commit=True)
    return render(request,'second_app/index.html', {'form':form,'access_records':web_list, 'access_car':web_car})

def CarForm_view(request):
    form = forms.CarForm()
    if request.method =='POST':
        form = forms.CarForm(request.POST)
        if form.is_valid():
            print("From validation is successfull, print in console.")
            print("Name: "+str(form.cleaned_data['c_name']))
            print("model: "+form.cleaned_data['model'])
            form.save(commit=True)
    return render(request,'second_app/help.html', {'form':form})

def BikeForm_view(request):
    form = forms.BikeForm()
    if request.method =='POST':
        form = forms.BikeForm(request.POST)
        if form.is_valid():
            print("From validation is successfull, print in console.")
            print("Name: "+str(form.cleaned_data['b_name']))
            print("Price: "+str(form.cleaned_data['price']))
            form.save(commit=True)
    return render(request,'second_app/bike.html', {'form':form})
