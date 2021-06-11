from django.shortcuts import render

def showIndex(request):
    emp_info = {"idno":101,"name":"Ravi","salary":185000.00}
    return render(request,"main.html",emp_info)