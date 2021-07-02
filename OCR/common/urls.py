
from django.urls import path
from common import views

urlpatterns = [
    path('',views.showCommonPage,name='common_page'),
    path('intern/',views.internPage,name='intern'),
    path('mentor/',views.mentorPage,name='mentor'),
    path('admin/',views.adminPage,name='admin'),
    path('contactus/',views.contactusPage,name='contactus'),
    path('intern_registration/',views.internRegistration,name='intern_registration'),

    path('intern_otp/',views.openinternOtp,name='intern_otp'),
    path('intern_login_check/',views.internLoginCheck,name='intern_login_check'),
    path('validate_otp/',views.validateOtp,name='validate_otp'),
]
