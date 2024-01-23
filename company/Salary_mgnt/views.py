from django.shortcuts import render,redirect
from django.http import HttpResponse
from Salary_mgnt.models import salary

# Create your views here.

def reps(request, sal_id):

    sall=salary.objects.all()
    
    context = {
        'sall':sall,
        'salid':sal_id
    }

    return render(request,'Salary_mgnt/reps.html', context)
