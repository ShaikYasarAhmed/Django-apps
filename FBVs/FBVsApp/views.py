from django.shortcuts import render,redirect
from FBVsApp.forms import EmployeeForm
from FBVsApp.models import Employee

# Create your views here.
def show_view(request):
    employees=Employee.objects.all()
    return render(request,'index.html',{'employees':employees})

def insert_view(request):
    form=EmployeeForm()
    if request.method=='POST':
       form=EmployeeForm(request.POST)
       if form.is_valid():
           form.save()
       return redirect('/show')
    return render(request,'insert.html',{'form':form})
def update_view(request,id):
    form=EmployeeForm()
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
           form.save()
           return redirect('/show')
    return render(request,'update.html',{'employee':employee})
def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')
def index_view(request):
    emp1=Employee.objects.get_queryset('esal')
    my_dict={'emp1':emp1}
    return render(request,"index.html",my_dict)
