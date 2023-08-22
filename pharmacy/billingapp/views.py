from django.shortcuts import render, redirect
from .forms import PatientForm

def submit_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PatientForm()
    return render(request, 'billingapp/submit_patient.html', {'form': form})

def success(request):
    return render(request, 'billingapp/success.html')

