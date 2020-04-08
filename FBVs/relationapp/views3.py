from django.shortcuts import render
from relationapp.models import Employee,ProxyEmployee,ProxyEmployee2
# Create your views here.
def display_view3(request):
    employees=ProxyEmployee2.objects.all()
    my_dict={'employees':employees}
    return render(request,"index.html",my_dict)
