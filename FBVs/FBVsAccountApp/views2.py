from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg,Sum,Max,Min,Count
from FBVsApp.models import Employee
# Create your views here.
def display_view(request):
    avg1=Employee.objects.all().aggregate(Avg('esal'))
    max=Employee.objects.all().aggregate(Max('esal'))
    min=Employee.objects.all().aggregate(Min('esal'))
    sum=Employee.objects.all().aggregate(Sum('esal'))
    count=Employee.objects.all().aggregate(Count('esal'))
    my_dict={'avg':avg1,'max':max,'min':min,'sum':sum,'count':count}
    return render(request,"aggregate.html",my_dict)
def index_view(request):
    emp1=Employee.objects.get_employees_sorted_by('esal')
    my_dict={'emp1':emp1}
    return render(request,"index.html",my_dict)
