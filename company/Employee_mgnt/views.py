from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.
def emp(request):
    return HttpResponse("This is Employee_mgnt page")