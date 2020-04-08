from django.db import models

# Create your models here.
class CustomManager(models.Manager):
  def get_employees_sorted_by(esal):
     return super().get_queryset().order_by('esal')
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.CharField(max_length=64)
    eaddr=models.CharField(max_length=256)
    objects=CustomManager()
