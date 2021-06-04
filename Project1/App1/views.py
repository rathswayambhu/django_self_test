from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
    message = "Hello Django Students"
    return HttpResponse(message)
