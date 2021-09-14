
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index,name='index'),
    path('form_name/',views.form_name_view, name='form_name'),
    path('webpage/',views.webpage_view, name='webpage'),
    path('webdate/',views.webdate_view, name='webdate'),
    #path('laptop', views.laptop_view),
    #path('college', views.college),
]
