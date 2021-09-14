import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from second_app.models import vehicle,car,bike
from faker import Faker

fakegen = Faker()
comp = ['benz','bmw','ferrari','maruthi']
topics = ['car', 'bike', 'auto', 'bus']

def add_topic():
    t = vehicle.objects.get_or_create(company=random.choice(comp))[0]
    t.save()
    return t

def populate(N=8):
    for entry in range(N):
        top = add_topic()

        fake_price = fakegen.localized_ean(length=8)
        fake_model = fakegen.company()
        #new webpage entry
        car1 = car.objects.get_or_create(c_name=top, model=fake_model)[0] #top-object of add_topic()
        #new  Webdate entry
        acc_bike = bike.objects.get_or_create(b_name=car1, price=fake_price)[0] #webpg - object

if __name__ == '__main__':
    print("populating script.")
    populate(10)
    print("populating complete.")
