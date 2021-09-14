from django.shortcuts import render
from django.http import HttpResponse
from . import forms
#from form import FormName           ...if from . import forms use this , not required to import FormName

from first_app.models import Topic, Webpage, Webdate

# Create your views here.
def index(request):
    '''my_dict = {'import_text':'This is my first application'}
    return render(request,"first_app/index.html",context=my_dict)'''

    web_list = Webdate.objects.order_by('access_date')
    my_dict = {'access_records':web_list}
    return render(request,"first_app/index.html",context=my_dict)

def laptop_view(request):
    return render(request, "first_app/lapTop.html")

def college(request):
    my_clg ={'clg_name':'CHMM COLLEGE FOR ADVANCED STUDIES.'}
    return render(request,"first_app/college.html",context=my_clg)

#.......form views......

def form_name_view(request):
    form = forms.FormName()
    #check to see if get a post back.
    if request.method =='POST':
        #in which case we pass in that request.
        form = forms.FormName(request.POST)
        #check to see form is valid.
        print("...............")
        if form.is_valid():
            #do something
            print("From validation is successfull, print in console.")
            print("Topic Name: "+form.cleaned_data['topic_name'])

            form.save(commit=True)
    return render(request,'first_app/form_name.html', {'form':form})

def webpage_view(request):
    form = forms.WebpageForm()
    #check to see if get a post back.
    if request.method =='POST':
        #in which case we pass in that request.
        form = forms.WebpageForm(request.POST)
        #check to see form is valid.
        print("...............")
        if form.is_valid():
            #do something
            print("From validation is successfull, print in console.")
            print("Topic Name: "+str(form.cleaned_data['category']))
            print("Name: "+form.cleaned_data['name'])
            print("URL: "+form.cleaned_data['url'])
            form.save(commit=True)
    return render(request,'first_app/webpage.html', {'form':form})

def webdate_view(request):
    form = forms.WebdateForm()
    if request.method =='POST':
        form = forms.WebdateForm(request.POST)
        if form.is_valid():
            print("From validation is successfull, print in console.")
            print("Name: "+str(form.cleaned_data['category']))
            print("Access_date: "+str(form.cleaned_data['access_date']))
            form.save(commit=True)
    return render(request,'first_app/webdate.html', {'form':form})
