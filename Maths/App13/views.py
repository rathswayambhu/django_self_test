from django.shortcuts import render
from django.http import HttpResponse
import mathfilters

def doMaths(request):
    value1 = request.POST.get("v1")
    value2 = request.POST.get("v2")


    return HttpResponse()