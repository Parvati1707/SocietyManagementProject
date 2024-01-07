from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from random import randint
from .models import *
from django.db import IntegrityError


def Send_OTP(request):
    otp=randint(1000,9999)
    request.session['otp']=otp
    send_to=[request.session['email']]
    send_from=settings.EMAIL_HOST_USER
    subject="Login Attemp"
    message=f"Hello! We Notice Activity in Email. OTP is :{otp}"

    print(request.session["otp"])

    send_mail(subject, message, send_from, send_to)

# Create your views here.
Home_Page_Link="Home_Page.html"
Login_Page_Link="validation/Login_Page.html"
Registration_Page_Link="validation/Registration_Page.html"
Forgate_Password_Page_Link="validation/Forgate_Password_Page.html"
OTP_Page_Link="validation/OTP_Page.html"

#Citizen Pages..

Citizen_Registration_Page_Link="Citizen/Citizen_Registration.html"
Citizen_Profile_Page_Link="Citizen/Citizen.html"

#Committee Pages..
Committee_Registration_Page_Link="Committee/Committee_Registration.html"
Committee_Profile_Page_Link="Committee/Committee.html"

#Security Pages..
Security_Registration_Page_Link="Security/Security_Registration.html"
Security_Profile_Page_Link="Security/Security.html"

#Admin Pages..

                                        # Start: Website Pages.. 

def Index(request):
    return render(request,Home_Page_Link)

def Login_Page(request):
    return render(request,Login_Page_Link)

def Registration_Page(request):
    return render(request,Registration_Page_Link)

def Forgate_Password_Page(request):
    return render(request,Forgate_Password_Page_Link)

def OTP_Page(request):
    return render(request,OTP_Page_Link)

def Citizen_Registration_Page(request):
    return render(request,Citizen_Registration_Page_Link)

def Committee_Registration_Page(request):
    return render(request,Committee_Registration_Page_Link)

def Security_Registration_Page(request):
    return render(request,Security_Registration_Page_Link)

def Citizen_Profile_Page(request):
    return render(request,Citizen_Profile_Page_Link)

def Committee_Profile_Page(request):
    return render(request,Committee_Profile_Page_Link)

def Security_Profile_Page(request):
    return render(request,Security_Profile_Page_Link)



                                        # End: Website Pages..

                                        #Start: Validation ...

def Login_Validation(request):
    login=SingUp.objects.get(Username=request.POST["Username"],Password=request.POST["password"])
    request.session['Username']=login.Username
    if login.Is_Admin==True:
        Send_OTP(request)
        return render(request,"Admin.html")
    elif login.Is_Citizen==True:
        request.session['login']=login.Username
        Send_OTP(request)
        return redirect(Citizen_Profile_Page)
    elif login.Is_Committee==True:
        request.session['login']=login.Username
        Send_OTP(request)
        return redirect(Committee_Profile_Page)
    elif login.Is_Security==True:
        request.session['login']=login.Username
        Send_OTP(request)
        return redirect(Security_Profile_Page)
    else:
        print("You are Not Register ")
        return redirect(Login_Page)

    return render(request,Login_Page)


def Registration_Validation(request):
    rl=["Citizen","Security","Admin","Committee"]

    if request.method=="POST":
        Role=request.POST.getlist('role') 
        print(Role)
        if Role==['Admin']:
            Register=SingUp.objects.create(Username=request.POST["UserName"],Password=request.POST["password"],Is_Admin=True)
            #return redirect(Login_page)
            print("Role is Admin") 
        elif Role==['Committee']:
            Register=SingUp.objects.create(Username=request.POST["UserName"],Password=request.POST["password"],Is_Committee=True)
            Committee_Registration.objects.create(singup=Register)
            request.session["Register"]=Register.Username
            print("Role is Committee")
            return redirect(Committee_Registration_Page)
        elif Role==['Citizen']:
            Register=SingUp.objects.create(Username=request.POST["UserName"],Password=request.POST["password"],Is_Citizen=True)
            Citizen_Registration.objects.create(singup=Register)
            request.session["Register"]=Register.Username
            print("Role is Citizen")
            return redirect(Citizen_Registration_Page)            
        elif Role==['Security']:
            Register=SingUp.objects.create(Username=request.POST["UserName"],Password=request.POST["password"],Is_Security=True)
            Security_Registration.objects.create(singup=Register)
            request.session["Register"]=Register.Username
            print("Role is Security")
            return redirect(Security_Registration_Page)
        else:
            print("Plese Select role")      
    return redirect(Registration_Page)

def Forgate_Password_Validation(request):
    login=SingUp.objects.get(Username=request.session['Username'])
    if login.Is_Citizen==True:
        citizen=Citizen_Registration.objects.get(singup=login,Email=request.POST["email"])
        request.session['email']=citizen.Email
        Send_OTP(request)
        return redirect(OTP_Page)

    return redirect(Forgate_Password_Page)


def OTP_varification(request):
    if int(request.POST["OTP"]==request.session['otp']):
        print("Message",request.session['otp'])
        login=SingUp.objects.get(Username=request.session['Username'])
        if login.Is_Admin==True:
            return render(request,"Admin.html")
        elif login.Is_Citizen==True:
            return redirect(Citizen_Profile_Page)
        elif login.Is_Committee==True:
            return redirect(Committee_Profile_Page)
        elif login.Is_Security==True:
            return redirect(Security_Profile_Page)

    return redirect(OTP_Page)

def Change_Password_Validation(request):
    pass

def Citizen_Validation(request):
    register=SingUp.objects.get(Username=request.session["Register"])
    citizen=Citizen_Registration.objects.get(singup=register)
    citizen.TotalMembers=BlockNo=request.POST["TotalFamilyMembers"]
    citizen.BlockNo=request.POST["blockno"]
    citizen.HouseNo=request.POST["houseno"]
    citizen.Contact=request.POST["phone"]
    citizen.Contac2t=request.POST["phone2"]
    citizen.AdharNumber=request.POST["Adhar"]
    citizen.BirthDate=request.POST["DOB"]
    citizen.Address=request.POST["address"]
    citizen.FirstName=request.POST["fname"]
    citizen.LastName=request.POST["lname"]
    citizen.Email=request.POST["email"]
    citizen.Gender=request.POST["gender"]
    citizen.Profession=request.POST["Prof"]
    citizen.Resident_Type=request.POST["Resident"]

    citizen.save()

    return redirect(Login_Page)


def Committee_Validation(request):
    register=SingUp.objects.get(Username=request.session["Register"])
    committee=Committee_Registration.objects.get(singup=register)
    committee.Email=request.POST["email"]
    committee.AdharNumber=request.POST["Adhar"]
    committee.BirthDate=request.POST["DOB"]
    committee.Contact=request.POST["phone"]
    committee.Gender=request.POST["gender"]
    committee.save()
    
    return redirect(Login_Page)

def Security_Validation(request):
    register=SingUp.objects.get(Username=request.session["Register"])
    security=Security_Registration.objects.get(singup=register)
    security.Email=request.POST["email"]
    security.AdharNumber=request.POST["Adhar"]
    security.BirthDate=request.POST["DOB"]
    security.Contact=request.POST["phone"]
    security.Gender=request.POST["gender"]
    security.save()

    return redirect(Login_Page)



                                        #End: Validation ...
                                     




