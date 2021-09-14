import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from third_app.models import country
from faker import Faker

fakegen = Faker()
def populate(N=5):
    for entry in range(N):
        #create fake data from entry
        fake_name = fakegen.first_name()
        fake_currency = fakegen.cryptocurrency_code()
        fake_bank = fakegen.bank_country()
        #new webpage entry
        use = country.objects.get_or_create(name=fake_name, currency=fake_currency, bank=fake_bank)[0] #top-object of add_topic()pytho

if __name__ == '__main__':
    print("populating script.")
    populate(20)
    print("populating complete.")
