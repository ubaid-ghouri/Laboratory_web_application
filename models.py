from django.db import models

# Create your models here.

class Patient(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    age=models.IntegerField()

class ClinicalData(models.Model):
    COMPONENT_NAME=[('hr','Heart Rate'),('bp','Blood Pressur'),('hw','Weight/Height')]
    componentName=models.CharField(choices=COMPONENT_NAME,max_length=20)
    componentValue=models.CharField(max_length=20)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date_Time=models.DateField()

