from django.db import models
# Create your models here.
class CustomManager1(models.Manager):
    def get_queryset(self):
      return super().get_queryset().filter(esal__gte=15000)
class CustomManager2(models.Manager):
    def get_queryset(self):
      return super().get_queryset().order_by('ename')
class CustomManager3(models.Manager):
    def get_queryset(self):
      return super().get_queryset().filter(eno__lt=1000)
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)
    objects=CustomManager1()
class ProxyEmployee(Employee):
    objects=CustomManager2()
    class Meta:
      proxy=True
class ProxyEmployee2(Employee):
    objects=CustomManager3()
    class Meta:
      proxy=True
