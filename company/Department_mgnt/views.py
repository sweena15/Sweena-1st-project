from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from Department_mgnt.models import dept
from Department_mgnt.models import Hierarchy
# Create your views here.
# def dep(request):
#     return HttpResponse("This is Department_mgnt page")

# def rep(request):
    
#     depl1=dept.objects.filter(Dep_head='Alexa')
#     depl2=dept.objects.filter(Dep_head='Mitesh')
#     context={
#         'depl1':depl1,
#         'depl2':depl2
#     }
#     return render(request,'Department_mgnt/rep.html',context)

def heir(request,heir_id):
    heir1=Hierarchy.objects.all()
    context={
        'heir1':heir1,
        'heirid':heir_id
    }
    return render(request,'Department_mgnt/rep.html',context)