import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fbvproject1.settings')
import django
django.setup()

from FBVsApp.models import*
from faker import faker
from random import*
faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randit(10000,20000)
        feaddr=faker.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
        populate(10)
