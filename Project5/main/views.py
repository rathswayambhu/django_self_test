from django.shortcuts import render

def showIndex(request):
    return render(request,"main.html")
    
