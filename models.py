from django.db import models
class CustomManager(models.Manager):
  def get_queryset(self):
     return super().get_queryset.order_by('eno')
  def get_emp_sal_range(self,esal1,esal2):
     return super().get_queryset().filter(esal__range=(esal1,esal2))
  def get_employees_sorted_by(self,param):
     return super().get_queryset().order_by(param)
# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)
