from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def loginCheck(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")

    if username == "Swayam" and password == "pwd123":
        return render(request,"welcome.html")
    else:
        return render(request,"error.html")