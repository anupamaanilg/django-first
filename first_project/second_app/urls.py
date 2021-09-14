
from django.urls import path
from second_app import views

urlpatterns = [
    path('', views.index,name='index'),
    path('car/',views.CarForm_view, name='car'),
    path('bike/',views.BikeForm_view, name='bike'),
]
