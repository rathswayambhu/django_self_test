from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from intern.models import RegistrationModel
from common.utils import sendTextMessage
from random import randint
from django.db.models import Q
from django.contrib import messages



def showCommonPage(request):
    return render(request,"common/index.html")


def internPage(request):
    return render(request,"common/intern.html")


def internRegistration(request):
    if request.method == "POST":
        name = request.POST.get("intern_name")
        contact = request.POST.get("intern_contact")
        email = request.POST.get("intern_email")
        password = request.POST.get("intern_password")

        record = RegistrationModel.objects.filter(Q(contact=contact) | Q(email=email))

        if record:
            return render(request, "common/intern.html",{"data": [name, contact, email, "Contact or Email already exists"]})
        else:
            otp = randint(100000, 999999)

            message = '''Thank you for reaching Swayam's Technologies,
            Your OTP for registration is  ''' + str(otp)

            if sendTextMessage(message, contact):
                RegistrationModel(name=name, contact=contact, email=email, password=password, otp=otp).save()

                messages.success(request, contact)

                return redirect('intern_otp')

            else:
                return render(request, "common/intern.html", {"data": [name, contact, email, "Wrong Contact Number", "Not Registered"]})
    else:
        internPage(request)

def openinternOtp(request):
    return render(request, "common/otp.html")

def internLoginCheck(request):
    if request.method == "POST":
        email = request.POST.get("intern_email")
        password = request.POST.get("intern_password")
        return HttpResponse("Under Development")
    else:
        return render(request, "common/intern.html")

def validateOtp(request):
    contact = request.POST.get("contact")
    sotp = request.POST.get("intern_otp")

    try:
        record = RegistrationModel.objects.get(contact=contact, otp=sotp)
        record.status = 'Active'
        record.save()
        return render(request, "common/intern.html", {"message": "Thanks For Registration, Please Login"})
    except RegistrationModel.DoesNotExist:
        messages.success(request, contact)
        return redirect('intern_otp')

def mentorPage(request):
    return render(request,"common/mentor.html")

def adminPage(request):
    return render(request,"common/admin.html")

def contactusPage(request):
    return render(request,"common/contactus.html")