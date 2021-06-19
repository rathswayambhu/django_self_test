from django.shortcuts import render

def showIndex(request):
    if request.method == "POST":
        username = request.POST.get("t1")
        password = request.POST.get("t2")
        if username == "Swayam" and password == "pwd123":
            return render(request,"index.html",{"message":"valid"})
        else:
            return render(request,"index.html",{"message":"invalid"})
    if request.method == "GET":
        return render(request,"index.html")
