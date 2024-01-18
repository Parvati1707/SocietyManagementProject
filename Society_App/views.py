from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from random import randint
from .models import *
from django.db import IntegrityError
from django.contrib import messages


def Send_OTP(request):
    otp=randint(1000,9999)
    request.session['otp']=otp
    send_to=[request.session['email']]
    send_from=settings.EMAIL_HOST_USER
    subject="Login Attemp"
    message=f"Hello! We Notice Activity in Email. OTP is :{otp}"

    print(request.session["otp"])
    send_mail(subject, message, send_from, send_to)

default_Dict={}
# Create your views here.
Home_Page_Link="Home_Page.html"
Login_Page_Link="validation/Login_Page.html"
Registration_Page_Link="validation/Registration_Page.html"
Forgate_Password_Page_Link="validation/Forgate_Password_Page.html"
OTP_Page_Link="validation/OTP_Page.html"

                                #Citizen Pages..

Citizen_Registration_Page_Link="Citizen/Citizen_Registration.html"
Citizen_Profile_Page_Link="Citizen/Citizen_Profile.html"
Citizen_Account_Setting_Page_Link="Citizen/Acount_Setting.html"
Booking_Request_Page_Link="Citizen/Booking_Request.html"
Complain_Page_Link="Citizen/Complain.html"
Rent_House_Page_Link="Citizen/Rent_House.html"
Sell_House_Page_Link="Citizen/Sell_House.html"
View_Events_Page_Link="Citizen/View_Events.html"
View_Notice_Page_Link="Citizen/View_Notice.html"

                                #Committee Pages..

Committee_Registration_Page_Link="Committee/Committee_Registration.html"
Committee_Profile_Page_Link="Committee/Committee_Profile.html"
Arrange_Meeting_Page_Link="Committee/Arrange_Meeting.html"
Committee_Account_Setting_Page_Link="Committee/Committee_Account_Setting.html"
Add_Event_Page_Link="Committee/Add_Event.html"
Add_Notice_Page_Link="Committee/Add_Notice.html"
Manage_complain_Page_Link="Committee/Manage_complain.html"
Display_Owner_Information_Page_Link="Committee/Owner_info.html"
Raise_Fund_Request_Page_Link="Committee/Raise_Fund_Request.html"


                                #Security Pages..

Security_Registration_Page_Link="Security/Security_Registration.html"
Security_Profile_Page_Link="Security/Security_Profile.html"
Guest_entry_Page_Link="Security/Guest_entry.html"
Security_Account_Setting_Page_Link="Security/Security_Account_Setting.html"
Make_Complain_Page_Link="Security/Security_Complain.html"




#--------------------------------------------------------------------------------------------------------------                                    


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

def Security_Profile_Page(request):
    return render(request,Security_Profile_Page_Link)




#--------------------------------------------------------------------------------------------------------------                                      
                                        # End: Website Pages..


                                        #Start: Citizen Related Page ...     
#-------------------------------------------------------------------------------------------------------------- 

def Citizen_Profile_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    Contaxt={
        "citizen":citizen
    }

    return render(request,Citizen_Profile_Page_Link,Contaxt)
                                                                 
def Citizen_Account_Setting_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    citizen.BirthDate=citizen.BirthDate.strftime('%Y-%m-%d')
    Contaxt={
        "citizen":citizen
    }
    print(Contaxt)
    return render(request,Citizen_Account_Setting_Page_Link,Contaxt)

def Rent_House_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    Contaxt={
        "citizen":citizen
    }
    return render(request,Rent_House_Page_Link,Contaxt)

def Sell_House_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    Contaxt={
        "citizen":citizen
    }
    return render(request,Sell_House_Page_Link,Contaxt)

def Citizen_Complain(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    Contaxt={
        "citizen":citizen
    }
    return render(request,Complain_Page_Link,Contaxt)

def Booking_Request_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    Contaxt={
        "citizen":citizen
    }
    return render(request,Booking_Request_Page_Link,Contaxt)

def View_Notice_Page(request):
    return render(request,View_Notice_Page_Link)

def View_Events_Page(request):
    return render(request,View_Events_Page_Link)



#--------------------------------------------------------------------------------------------------------------                                      
                                        # End: Citizen Related Page..


                                        #Start: Committee Related Page ...
#-------------------------------------------------------------------------------------------------------------- 


def Committee_Profile_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Contaxt={
        "committee":committee
    }

    return render(request,Committee_Profile_Page_Link,Contaxt)

def Committee_Account_Setting(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    committee.BirthDate=committee.BirthDate.strftime('%Y-%m-%d')
    Contaxt={
        "committee":committee
    }
    return render(request,Committee_Account_Setting_Page_Link,Contaxt)

def Arrange_Meeting(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Contaxt={
        "committee":committee
    }
    return render(request,Arrange_Meeting_Page_Link,Contaxt)
 

def Raise_fund_Request_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Contaxt={
        "committee":committee
    }
    return render(request,Raise_Fund_Request_Page_Link,Contaxt)

def Add_Notice_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Contaxt={
        "committee":committee
    }
    return render(request,Add_Notice_Page_Link,Contaxt)

def Add_Event_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Contaxt={
        "committee":committee
    }
    return render(request,Add_Event_Page_Link,Contaxt)


#--------------------------------------------------------------------------------------------------------------                                                            
                                    # End: Committee Related Page..


                                    # Start: Security Related Page..
#-------------------------------------------------------------------------------------------------------------- 

def Security_Account_Setting_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    security=Security_Registration.objects.get(singup=login)
    security.BirthDate=security.BirthDate.strftime('%Y-%m-%d')
    Contaxt={
        "security":security
    }
    return render(request,Security_Account_Setting_Page_Link,Contaxt)

def Guest_Entry_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    security=Security_Registration.objects.get(singup=login)
    Contaxt={
        "security":security
    }
    return render(request,Guest_entry_Page_Link,Contaxt)

def Security_Complain(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    security=Security_Registration.objects.get(singup=login)
    Contaxt={
        "security":security
    }
    return render(request,Make_Complain_Page_Link,Contaxt)




#-------------------------------------------------------------------------------------------------------------- 
                                    # Start: Security Related Page..
                                    
                                     
                                        #Start: Validation ...
#-------------------------------------------------------------------------------------------------------------- 
def Login_Validation(request):   
    try:
        login=SingUp.objects.get(Username=request.POST["Username"])
        
        if login.Password==request.POST["password"]:
            if login.Is_Admin==True:
                request.session['Login_Name']=login.Username
                return render(request,"Admin.html")

            elif login.Is_Citizen==True:
                request.session['Login_Name']=login.Username       
                return redirect(Citizen_Profile_Page)

            elif login.Is_Committee==True:
                request.session['Login_Name']=login.Username
                return redirect(Committee_Profile_Page)

            elif login.Is_Security==True:
                request.session['Login_Name']=login.Username
                return redirect(Security_Profile_Page)

            else:
                print("You are Not Register ")
                return redirect(Login_Page)
        else:
            messages.warning(request,"Incorrect Password")
            return redirect(Login_Page)
    except:
        messages.warning(request,"Incorrect Username")
        return redirect(Login_Page)

    return render(request,Login_Page)

def Load_Profile(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    if login.Is_Citizen==True:
        citizen=Citizen_Registration.objects.get(singup=login)
        default_Dict["profile_data"]=citizen
    elif login.Is_Committee==True:
        committee=Committee_Registration.objects.get(singup=login)
        default_Dict["profile_data"]=committee
    elif login.Is_Security==True:
        security=Security_Registration.objects.get(singup=login)
        default_Dict["profile_data"]=security
    else:
        messages.warning(request,"Session is not created")
        return redirect(Login_Page)

def Logout(request):
    print(request.session['Login_Name'])
    del request.session['Login_Name']
    return redirect(Login_Page)

def Registration_Validation(request):
   # rl=["Citizen","Security","Admin","Committee"]

    if request.method=="POST":
        Role=request.POST.getlist('role') 
        print(Role)
        
        if request.POST["password"]!=request.POST["Coinfirmpassword"]:
            messages.warning(request,"Password Doesn't Match")
            return redirect(Registration_Page)

        try:
            if SingUp.objects.get(Username=request.POST["UserName"]):
                messages.warning(request,"Username Already Exist")
                return redirect(Registration_Page)
        except:
            pass
        
        if Role==['Admin']:
            Register=SingUp.objects.create(Username=request.POST["UserName"],Password=request.POST["password"],Email=request.POST["Email"],Is_Admin=True)
            #return redirect(Login_page)
            print("Role is Admin") 
        elif Role==['Committee']:
            Register=SingUp.objects.create(Username=request.POST["UserName"],Password=request.POST["password"],Email=request.POST["Email"],Is_Committee=True)
            Committee_Registration.objects.create(singup=Register)
            request.session["Register"]=Register.Username
            print("Role is Committee")
            return redirect(Committee_Registration_Page)
        elif Role==['Citizen']:
            Register=SingUp.objects.create(Username=request.POST["UserName"],Password=request.POST["password"],Email=request.POST["Email"],Is_Citizen=True)
            Citizen_Registration.objects.create(singup=Register)
            request.session["Register"]=Register.Username
            print("Role is Citizen")
            return redirect(Citizen_Registration_Page)            
        elif Role==['Security']:
            Register=SingUp.objects.create(Username=request.POST["UserName"],Password=request.POST["password"],Email=request.POST["Email"],Is_Security=True)
            Security_Registration.objects.create(singup=Register)
            request.session["Register"]=Register.Username
            print("Role is Security")
            return redirect(Security_Registration_Page)
        else:
            messages.warning(request,"Please Select Role")
            return redirect(Registration_Page)     
    return redirect(Registration_Page)

def Forgate_Password_Validation(request):
    try:
        login=SingUp.objects.get(Username=request.POST["Username"])  
        request.session['Login_Name']=login.Username 
        if login.Email == request.POST["email"]:   
            request.session['email']=login.Email
            Send_OTP(request)
            return redirect(OTP_Page)   
        else:
            messages.warning(request,"Please Enter a valid email")
            return redirect(Forgate_Password_Page)          
    except:
        messages.warning(request,"Username Not Exist")
        return redirect(Forgate_Password_Page)

    return redirect(Forgate_Password_Page)

def OTP_varification(request):
    print("MEass",request.session["otp"])
    if int(request.POST["OTP"])==request.session["otp"]:
        login=SingUp.objects.get(Email=request.session['email'])
        if login.Is_Citizen:
            return redirect(Citizen_Profile_Page)
        elif login.Is_Committee:
            return redirect(Committee_Profile_Page)
        elif login.Is_Security:
            return redirect(Security_Profile_Page)
    else:
        messages.warning(request,"Incorrect OTP")
        return redirect(OTP_Page)

    return redirect(OTP_Page)

def Change_Password_Of_Citizen(request):
    try:
        login=SingUp.objects.get(Username=request.session['Login_Name'])
        
        if login.Password == request.POST["current_Password"]:
            
            if request.POST["new_password"] == request.POST["confirm_password"]:
                print(login.Password)
                login.Password = request.POST["new_password"]
                login.save()
                messages.warning(request,"Password Change Succssfully")
                return redirect(Citizen_Account_Setting_Page)
            else:
                messages.warning(request,"Both Password Not Match....")
                return redirect(Citizen_Account_Setting_Page)
        else:
            messages.warning(request,"Invalid Password")
            return redirect(Citizen_Account_Setting_Page)

        return redirect(Citizen_Account_Setting_Page)
    except:
        pass

def Change_Password_Of_Committee(request):
    try:
        login=SingUp.objects.get(Username=request.session['Login_Name'])
        
        if login.Password == request.POST["current_Password"]:
            
            if request.POST["new_password"] == request.POST["confirm_password"]:
                print(login.Password)
                login.Password = request.POST["new_password"]
                login.save()
                messages.warning(request,"Password Change Succssfully")
                return redirect(Committee_Account_Setting)
            else:
                messages.warning(request,"Both Password Not Match....")
                return redirect(Committee_Account_Setting)
        else:
            messages.warning(request,"Invalid Password")
            return redirect(Committee_Account_Setting)

        return redirect(Committee_Account_Setting)
    except:
        pass

def Change_Password_Of_Security(request):
    try:
        login=SingUp.objects.get(Username=request.session['Login_Name'])
        
        if login.Password == request.POST["current_Password"]:
            
            if request.POST["new_password"] == request.POST["confirm_password"]:
                print(login.Password)
                login.Password = request.POST["new_password"]
                login.save()
                messages.warning(request,"Password Change Succssfully")
                return redirect(Security_Account_Setting_Page)
            else:
                messages.warning(request,"Both Password Not Match....")
                return redirect(Security_Account_Setting_Page)
        else:
            messages.warning(request,"Invalid Password")
            return redirect(Security_Account_Setting_Page)

        return redirect(Security_Account_Setting_Page)
    except:
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
    citizen.Gender=request.POST["gender"]
    citizen.Profession=request.POST["Prof"]
    citizen.Resident_Type=request.POST["Resident"]

    citizen.save()

    return redirect(Login_Page)


def Committee_Validation(request):
    register=SingUp.objects.get(Username=request.session["Register"])
    committee=Committee_Registration.objects.get(singup=register)
    committee.AdharNumber=request.POST["Adhar"]
    committee.BirthDate=request.POST["DOB"]
    committee.Contact=request.POST["phone"]
    committee.Gender=request.POST["gender"]
    committee.save()
    
    return redirect(Login_Page)

def Security_Validation(request):
    register=SingUp.objects.get(Username=request.session["Register"])
    security=Security_Registration.objects.get(singup=register)    
    security.AdharNumber=request.POST["Adhar"]
    security.BirthDate=request.POST["DOB"]
    security.Contact=request.POST["phone"]
    security.Gender=request.POST["gender"]
    security.save()

    return redirect(Login_Page)                                   






#--------------------------------------------------------------------------------------------------------------                                      
                                            #End: Validation ...
                                 




