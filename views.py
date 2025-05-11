from django.shortcuts import render,redirect
from .models import Patient,ClinicalData
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from .forms import ClinicalDataForm

# Create your views here.
class PatientListView(ListView):
    model=Patient

class PatientUpdateView(UpdateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','age')

class PatientCreateView(CreateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','age')

class PatientDelete(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')

def getData(request,**kwargs):
    form=ClinicalDataForm()
    patient=Patient.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalsapp/clinicaldata.html',{'form':form,'patient':patient})

def analyseData(request,**kwargs):
    data=ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responsedata=[]
    for eachentry in data:
        if eachentry.componentName=='hw':
            HW=eachentry.componentValue.split('/')
            if len(HW)>1:
                height=float(HW[0])
                weight=float(HW[1])
                print(HW)
                BMI=(weight)/(height*height)
                bmiEntry=ClinicalData()
                bmiEntry.componentName='BMI'
                bmiEntry.componentValue=BMI
                responsedata.append(bmiEntry)
        responsedata.append(eachentry)
    return render(request,'clinicalsapp/dataanalysis.html',{'data':responsedata})


