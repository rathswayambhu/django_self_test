from django.shortcuts import render
from django.http import HttpResponse

def showIndex(request):
    return render(request,"index.html")

def registerUser(request):
    f_name = request.POST.get("t1")
    l_name = request.POST.get("t2")

    full_name = f_name+" "+l_name

    return HttpResponse(full_name)