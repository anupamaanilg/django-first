import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic,Webpage,Webdate
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'MarketPlace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        #create fake data from entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        #new webpage entry
        webpg = Webpage.objects.get_or_create(category=top, name=fake_name, url=fake_url)[0] #top-object of add_topic()
        #new  Webdate entry
        acc_date = Webdate.objects.get_or_create(category=webpg, access_date=fake_date)[0] #webpg - object

if __name__ == '__main__':
    print("populating script.")
    populate(20)
    print("populating complete.")
