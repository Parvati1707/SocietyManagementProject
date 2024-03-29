from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from random import randint
from .models import *
from django.db import IntegrityError
from django.contrib import messages
from django.db.models import Q


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
Home_Page_Link="LandingPage.html"
Login_Page_Link="validation/Login_Page.html"
Registration_Page_Link="validation/Registration_Page.html"
Forgate_Password_Page_Link="validation/Forgate_Password_Page.html"
OTP_Page_Link="validation/OTP_Page.html"

                                #Report Pages..

Report_Page_Link="ReportPages/Report_Page.html"

Society_Report_Page_Link="ReportPages/Society_Report.html"

Block_Report_Page_Link="ReportPages/Block_Report.html"

House_Report_Page_Link="ReportPages/House_Report.html"

Citizen_Report_Page_Link="ReportPages/Citizen_Report.html"

Complain_Report_Page_Link="ReportPages/Complain_Report.html"

Personal_Event_Booking_Page_Link="ReportPages/Booking_Request_Report.html"

Sell_Rent_Report_Page_Link="ReportPages/Sell_Rent_Report.html"

sreach_Result_Page_Link="ReportPages/Sreach_Result_Page.html"

                                #Admin Pages..

Admin_Profile_Page_Link="Admin/Admin_Profile.html"
Admin_Account_Setting_Page_Link="Admin/Admin_Account_Settings.html"
Add_Society_Page_Link="Admin/Add_Society.html"
Add_Block_Page_Link="Admin/Add_Blocks.html"
Add_Houses_Page_Link="Admin/Add_Houses.html" 
Manage_Complain_Page_Link="Admin/Manage_Complain.html"
Solve_Complain_Page_Link="Admin/Solve_complain_Page.html"


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
Society_Event_List_Page_Link="Committee/Event_List.html"
Add_Notice_Page_Link="Committee/Add_Notice.html"
Committee_Manage_complain_Page_Link="Committee/Manage_Complain.html"
Committee_solve_complain_Page_Link="Committee/Solve_complain_Page.html"
Display_Owner_Information_Page_Link="Committee/Owner_info.html"
Raise_Fund_Request_Page_Link="Committee/Raise_Fund_Request.html"
Booking_Request_List_Page_Link="Committee/Booking_Request_List.html"


                                #Security Pages..

Security_Registration_Page_Link="Security/Security_Registration.html"
Security_Profile_Page_Link="Security/Security_Profile.html"
Guest_entry_Page_Link="Security/Guest_entry.html"
Security_Account_Setting_Page_Link="Security/Security_Account_Setting.html"
Make_Complain_Page_Link="Security/Security_Complain.html"
Guest_Entry_List_Page_Link="Security/Entry_List.html"




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






#--------------------------------------------------------------------------------------------------------------                                      
                                        # End: Website Pages..


                                     #Start: Admin Related Page ...     
#-------------------------------------------------------------------------------------------------------------- 


def Admin_Profile_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    context={
        "Login":login
    }
    return render(request,Admin_Profile_Page_Link,context)

def Admin_Account_Setting_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    context={
        "Login":login
    }
    return render(request,Admin_Account_Setting_Page_Link,context)

def Update_Admin_Profile(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])

    login.Username=request.POST["Username"]
    login.Email=request.POST["Email"]

    login.save()

    return redirect(Login_Page)

def Add_Society_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    context={
        "Login":login
    }
    return render(request,Add_Society_Page_Link,context)

def Add_New_Society(request):
    try:
        if Add_Society.objects.get(Society_Name=request.POST["Society_Name"]):
            messages.warning(request,"Society Already Exist.....")
            return redirect(Add_Society_Page)        
    except:
        Society=Add_Society()
        Society.Society_Name=request.POST["Society_Name"]
        Society.Address=request.POST["Address"]
        Society.City=request.POST["City"]
        Society.PinCode=request.POST["Pincode"]
        Society.No_Of_House=request.POST["TotalHouses"]
        Society.Society_Image=request.FILES['Upload_image']
        Society.Entry_Date=request.POST["Entry_Date"]

        Society.save()

    return render(request,Add_Society_Page_Link)

def Add_New_Block_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    context={
        "Login":login
    }
    return render(request,Add_Block_Page_Link,context)

def Add_Block(request):
    try:
        if Add_Society.objects.get(Society_Name=request.POST["Society_Name"]):

            try:
                Society=Add_Society.objects.get(Society_Name=request.POST["Society_Name"])

                if Add_New_Block.objects.get(Society_Name=Society,Block_No=request.POST["Block_No"]):

                    messages.warning(request,"Block Already Exist")
                    return redirect(Add_New_Block_Page)                

            except:
                Society=Add_Society.objects.get(Society_Name=request.POST["Society_Name"])
                Block=Add_New_Block.objects.create(Society_Name=Society,Block_No=request.POST["Block_No"],NO_Of_Floors=request.POST["No_of_Floors"],No_Of_Flats=request.POST["No_of_Flats"])   

    except:
        messages.warning(request,"Entered Society Not Found")
        return redirect(Add_New_Block_Page)
    
    

    return redirect(Add_New_Block_Page)

def Add_Houses_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    context={
        "Login":login
    }
    return render(request,Add_Houses_Page_Link,context)

def Add_house(request):
    try:
        if Add_Society.objects.get(Society_Name=request.POST["Society_Name"]):

            try:

                Society=Add_Society.objects.get(Society_Name=request.POST["Society_Name"])    
                if Add_New_Block.objects.get(Society_Name=Society,Block_No=request.POST["Block_No"]):

                    try:
                        
                        Society=Add_Society.objects.get(Society_Name=request.POST["Society_Name"])    
                        Block=Add_New_Block.objects.get(Society_Name=Society,Block_No=request.POST["Block_No"])
                        
                        if Add_House.objects.get(Block_No=Block,House_No=request.POST["House_No"]):
                           
                            messages.warning(request,"House No. Already Exist...")
                            return redirect(Add_Houses_Page)  

                    except:
                        Society=Add_Society.objects.get(Society_Name=request.POST["Society_Name"])    
                        Block=Add_New_Block.objects.get(Society_Name=Society,Block_No=request.POST["Block_No"])
                        House=Add_House.objects.create(Society_Name=Society,Block_No=Block,House_No=request.POST["House_No"],Detail=request.POST["Details"],House_Type=request.POST["House_Type"],Image=request.FILES["Upload_image"],Entry_Date=request.POST["Entry_Date"])
    
            except:
                messages.warning(request,"Block Not Fount..")
                return redirect(Add_Houses_Page)  
    except:
        messages.warning(request,"Entered Society Not Found")
        return redirect(Add_Houses_Page) 

    return redirect(Add_Houses_Page) 

def Manage_Complain_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    complain=Complain.objects.all()
    context={
        'complain':complain,
        "Login":login
    }
    return render(request,Manage_Complain_Page_Link,context)

def Solve_Complain_page(request,id):    
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    complain=Complain.objects.get(id=id)
    context={
        'complain':complain,
        "Login":login
    }
    return render(request,Solve_Complain_Page_Link,context)

def Solve_Complain(request,id):
    complain=Complain.objects.get(id=id)

    complain.Status=request.GET["Status"]
    complain.save()

    return redirect(Manage_Complain_Page)



#-------------------------------------------------------------------------------------------------------------- 

                                         #End: Admin Related Page ...  


                                        #Start: Report Related Page ...     
#-------------------------------------------------------------------------------------------------------------- 



def Report_Page(request):
    Booking_Report=Personal_Event_Booking.objects.all()
    context={
        'Booking_Report':Booking_Report,
    }
    return render(request,Personal_Event_Booking_Page_Link,context)
    return render(request,Report_Page_Link)

def Society_Report_Page(request):
    Society_Report=Add_Society.objects.all()
    context={
        'Society_Report':Society_Report,

    }
    return render(request,Society_Report_Page_Link,context)

def Block_Report_Page(request):
    Block_Report=Add_New_Block.objects.all()
    context={
        'Block_Report':Block_Report,        
    }
    return render(request,Block_Report_Page_Link,context)

def House_Report_Page(request):
    House_Report=Add_House.objects.all()
    context={
        'House_Report':House_Report,
    }
    return render(request,House_Report_Page_Link,context)

def Complain_Report_Page(request):
    Complain_Report=Complain.objects.all()
    context={
        'Complain_Report':Complain_Report,
    }
    return render(request,Complain_Report_Page_Link,context)

def Personal_Event_Booking_Report_Page(request):
    Booking_Report=Personal_Event_Booking.objects.all()
    context={
        'Booking_Report':Booking_Report,
    }
    return render(request,Personal_Event_Booking_Page_Link,context)

def Sell_Rent_Report_Page(request):
    Sell_Report=Sell_House.objects.all()
    Rent_Report=Rent_House.objects.all()
    context={
        'Sell_Report':Sell_Report,
        'Rent_Report':Rent_Report
    }
    return render(request,Sell_Rent_Report_Page_Link,context)

def Citizen_Report_Page(request):
    Citizen_Report=Citizen_Registration.objects.all()
    context={
        'Citizen_Report':Citizen_Report,
    }
    return render(request,Citizen_Report_Page_Link,context)

def Sreach_Result_Page(request):
    query=request.GET["query"]

    if len(query)>78:
        Society_Sreach=Add_Society.objects.none
    else:

            # Society details Sreach
        Society_Sreach=Add_Society.objects.filter(Q(Society_Name__icontains=query) | Q(Address__icontains=query) | Q(City__icontains=query) | Q(PinCode__icontains=query) | Q(No_Of_House__icontains=query) | Q(Entry_Date__icontains=query))

            # Block Details Sreach
       
        Block_sreach=Add_New_Block.objects.filter(Q(Block_No__icontains=query) | Q(NO_Of_Floors__icontains=query) | Q(No_Of_Flats__icontains=query))

            # house Details

        House_Sreach=Add_House.objects.filter(Q(House_No__icontains=query) | Q(House_Type__icontains=query) | Q(Detail__icontains=query) | Q(Entry_Date__icontains=query))

            # Personal event Booking Info
        
        Event_Sreach=Personal_Event_Booking.objects.filter(Q(Event_Name__icontains=query) | Q(No_Of_Guest__icontains=query) | Q(Entry_Date__icontains=query))

            # Citizen Info

        Citizen_Sreach=Citizen_Registration.objects.filter(Q(TotalMembers__icontains=query) | Q(Resident_Type__icontains=query) | Q(FirstName__icontains=query) | Q(LastName__icontains=query) | Q(Gender__icontains=query) | Q(Profession__icontains=query) | Q(Contact__icontains=query) | Q(BlockNo__icontains=query) | Q(HouseNo__icontains=query))

            # Sell Sreach Detail

        Sell_Sreach=Sell_House.objects.filter(Q(Sell_Price__icontains=query) | Q(Entry_Date__icontains=query))

            # Rent Sreach Detail

        Rent_Sreach=Rent_House.objects.filter(Q(Rent_Price__icontains=query) | Q(Entry_Date__icontains=query))

            # complain Details

        Complain_sreach=Complain.objects.filter(Q(Subject__icontains=query) | Q(Status__icontains=query) | Q(Entry_Date__icontains=query))
        
    sreach={
        'Society_Sreach':Society_Sreach,
        'Block_sreach':Block_sreach,
        'House_Sreach':House_Sreach,
        'Event_Sreach':Event_Sreach,
        'Citizen_Sreach':Citizen_Sreach,
        'Sell_Sreach':Sell_Sreach,
        'Rent_Sreach':Rent_Sreach,
        'Complain_sreach':Complain_sreach,
        'query':query
    }
    return render(request,sreach_Result_Page_Link,sreach)



#-------------------------------------------------------------------------------------------------------------- 

                                         #End: Report Related Page ...  


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

def Update_citizen_Profile(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    citizen.TotalMembers=BlockNo=request.POST["TotalMembers"]
    citizen.BlockNo=request.POST["BlockNo"]
    citizen.HouseNo=request.POST["HouseNo"]
    citizen.Contact=request.POST["Phone"]
    citizen.Contac2t=request.POST["Phone2"]
    citizen.AdharNumber=request.POST["AdharNumber"]
    citizen.BirthDate=request.POST["birthday"]
    citizen.Address=request.POST["Address"]
    citizen.FirstName=request.POST["FirstName"]
    citizen.LastName=request.POST["LastName"]
    citizen.Gender=request.POST["gender"]
    citizen.Profession=request.POST["Profession"]
    citizen.Resident_Type=request.POST["Resident_Type"]

    citizen.save()

    return redirect(Citizen_Account_Setting_Page)

def Rent_House_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    Contaxt={
        "citizen":citizen
    }
    return render(request,Rent_House_Page_Link,Contaxt)

def Insert_Rent_House(request):
    try:
        if Add_Society.objects.get(Society_Name=request.POST["Society_Name"]):
            try:
                if Add_House.objects.get(House_No=request.POST["House_No"]):

                    login=SingUp.objects.get(Username=request.session['Login_Name'])
                    Society=Add_Society.objects.get(Society_Name=request.POST["Society_Name"])
                    House=Add_House.objects.get(House_No=request.POST["House_No"])
                                        
                    Rent=Rent_House.objects.create(Citizen_Id=login,Society_Id=Society,House_Id=House,Rent_Price=request.POST["Price"],Entry_Date=request.POST["Entry_Date"])
                    
                    messages.warning(request,"Succssfully Registered")
                    return redirect(Rent_House_Page) 

            except:
                messages.warning(request,"House Not Exist")
                return redirect(Rent_House_Page) 
    except:
        messages.warning(request,"Society Not Exist")
        return redirect(Rent_House_Page) 
                

    return redirect(Rent_House_Page)


def Sell_House_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    Contaxt={
        "citizen":citizen
    }
    return render(request,Sell_House_Page_Link,Contaxt)

def Insert_Sell_House(request):
    try:
        if Add_Society.objects.get(Society_Name=request.POST["Society_Name"]):
            try:
                if Add_House.objects.get(House_No=request.POST["House_No"]):

                    login=SingUp.objects.get(Username=request.session['Login_Name'])
                    Society=Add_Society.objects.get(Society_Name=request.POST["Society_Name"])
                    House=Add_House.objects.get(House_No=request.POST["House_No"])
                                        
                    Sell=Sell_House.objects.create(Citizen_Id=login,Society_Id=Society,House_Id=House,Sell_Price=request.POST["Price"],Entry_Date=request.POST["Entry_Date"])
                    
                    print("Saved")
            except:
                messages.warning(request,"House Not Exist")
                return redirect(Sell_House_Page) 
    except:
        messages.warning(request,"Society Not Exist")
        return redirect(Sell_House_Page) 
                

    return redirect(Sell_House_Page)

def Citizen_Complain(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    Contaxt={
        "citizen":citizen
    }
    return render(request,Complain_Page_Link,Contaxt)

def Insert_Complain(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    Type=Complain_Type.objects.get(Complain_Name=request.POST["Complain_type"])
    New_Complain=Complain.objects.create(Citizen_Id=login,Subject=request.POST["Subject"],Complain=Type,Entry_Date=request.POST["Entry_Date"])
    print(request.POST)
    print("Save")
    messages.warning(request,"Complain Registered ")

    return redirect(Citizen_Complain) 

def Booking_Request_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    Contaxt={
        "citizen":citizen
    }
    return render(request,Booking_Request_Page_Link,Contaxt)

def Insert_New_Request(request):
    try:
        if Add_Society.objects.get(Society_Name=request.POST["Society_Name"]):
            try:

                if Add_House.objects.get(House_No=request.POST["House_No"]):
                    login=SingUp.objects.get(Username=request.session['Login_Name'])
                    Society=Add_Society.objects.get(Society_Name=request.POST["Society_Name"])
                    House=Add_House.objects.get(House_No=request.POST["House_No"])

                    New_Request=Personal_Event_Booking.objects.create(House_Id=House,Society_Id=Society,Citizen_Id=login,Event_Name=request.POST["Event_Name"],No_Of_Guest=request.POST["Guest"],Entry_Date=request.POST["DateTime"])
                    
                    messages.warning(request,"Request Submited")
                    return redirect(Booking_Request_Page) 
            except:
                messages.warning(request,"House Not Exist")
                return redirect(Booking_Request_Page) 
    except:
        messages.warning(request,"Society Not Exist")
        return redirect(Booking_Request_Page)

    return redirect(Booking_Request_Page)             


def View_Notice_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    notice=Notice.objects.all()
    Contaxt={
        "citizen":citizen,
        "notice":notice,
    }
    return render(request,View_Notice_Page_Link,Contaxt)

def View_Events_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    society_event=Society_Event.objects.all()
    Contaxt={
        "citizen":citizen,
        "society_event":society_event,
    }
    return render(request,View_Events_Page_Link,Contaxt)



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

def Update_Committee_Profile(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    committee.AdharNumber=request.POST["adharnumber"]
    committee.BirthDate=request.POST["birthdate"]
    committee.Contact=request.POST["contact"]
    committee.Gender=request.POST["gender"]
    committee.save()
    
    return redirect(Committee_Account_Setting)

def Arrange_Meeting_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Contaxt={
        "committee":committee
    }
    return render(request,Arrange_Meeting_Page_Link,Contaxt)
 
def Insert_In_Arreage_Meeting(request):
    insert_arrange_meeting=Arrange_Meeting.objects.create(Meet_Agenda=request.POST["meeting_agenda"],DateTime=request.POST["meetingdatetime"],Meet_conclusion=request.POST["meeting_Conclusion"])
    
    messages.success(request,"Data Successfully Saved....")

    return redirect(Arrange_Meeting_Page)

def Raise_fund_Request_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Contaxt={
        "committee":committee
    }
    return render(request,Raise_Fund_Request_Page_Link,Contaxt)

def Insert_Raise_Fund_Request(request):
    Type=Fund_Type.objects.get(Fund_Name=request.POST["Fund_Type"])
    
    Insert_Fund_request=Raise_Fund.objects.create(Fund_Type=Type,DateTime=request.POST["datetime"])
    
    messages.success(request,"Data Successfully Saved....")

    return redirect(Raise_fund_Request_Page)

def Add_Notice_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Contaxt={
        "committee":committee
    }
    return render(request,Add_Notice_Page_Link,Contaxt)

def Insert_Notice(request):
    Type=Notice_Type.objects.get(Notice_Name=request.POST["Notice_Type"])

    insert_notice=Notice.objects.create(Notice=Type,Subject=request.POST["Notice_Subject"],DateTime=request.POST["notice_datetime"])

    messages.success(request,"Data Successfully Saved....")

    return redirect(Add_Notice_Page)

def Add_Event_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Contaxt={
        "committee":committee
    }
    return render(request,Add_Event_Page_Link,Contaxt)

def Society_Event_List_Page(request):
    event_list=Society_Event.objects.all()
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Context={
        "committee":committee,
        "Event_List":event_list
    }
    return render(request,Society_Event_List_Page_Link,Context)

def Insert_Event(request):
    Type=Event_Type.objects.get(Event_Name=request.POST["Event_Type"])

    insert_Event=Society_Event.objects.create(Event_Type=Type,DateTime=request.POST["Eventdatetime"])

    messages.warning(request,"Data Successfully Saved....")

    return redirect(Add_Event_Page)

def Committee_Manage_Complain_Page(request):
    Complain_List=Complain.objects.all()
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Context={
        'Complain_List':Complain_List,
        "committee":committee
    }
    return render(request,Committee_Manage_complain_Page_Link,Context)

def Committee_Solve_Complain_Page(request,id):
    complain=Complain.objects.get(id=id)
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Context={
        'complain':complain,
        "committee":committee
    }
    return render(request,Committee_solve_complain_Page_Link,Context)

def Committee_Solve_Complain(request,id):
    complain=Complain.objects.get(id=id)

    complain.Status=request.GET["Status"]
    complain.save()

    return redirect(Committee_Manage_Complain_Page)

def Booking_Request_List_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Request_List=Personal_Event_Booking.objects.all()

    Contaxt={
        "committee":committee,
        'Request_List':Request_List
    }
    return render(request,Booking_Request_List_Page_Link,Contaxt)

def Display_Owner_Information_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    Owner_Info=Citizen_Registration.objects.all()
    
    Contaxt={
        "committee":committee,
        'Owner_Info':Owner_Info
    }
    return render(request,Display_Owner_Information_Page_Link,Contaxt)
#--------------------------------------------------------------------------------------------------------------                                                            
                                    # End: Committee Related Page..


                                    # Start: Security Related Page..
#-------------------------------------------------------------------------------------------------------------- 
def Security_Profile_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    security=Security_Registration.objects.get(singup=login)
    security.BirthDate=security.BirthDate.strftime('%Y-%m-%d')
    Contaxt={
        "security":security
    }
    return render(request,Security_Profile_Page_Link,Contaxt)

def Security_Account_Setting_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    security=Security_Registration.objects.get(singup=login)
    security.BirthDate=security.BirthDate.strftime('%Y-%m-%d')
    Contaxt={
        "security":security
    }
    return render(request,Security_Account_Setting_Page_Link,Contaxt)

def Update_Security_Profile(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    security=Security_Registration.objects.get(singup=login)    
    security.AdharNumber=request.POST["AdharNumber"]
    security.BirthDate=request.POST["BirthDate"]
    security.Contact=request.POST["Contact"]
    security.Gender=request.POST["gender"]
    security.save()

    return redirect(Security_Account_Setting_Page)                                   

def Guest_Entry_Page(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    security=Security_Registration.objects.get(singup=login)
    Contaxt={
        "security":security
    }
    return render(request,Guest_entry_Page_Link,Contaxt)

def Insert_Guest_Entry(request):
    try:
        if Add_Society.objects.get(Society_Name=request.POST["Society_Name"]):
            login=SingUp.objects.get(Username=request.session['Login_Name'])
            New_Entry=Guest_Entry.objects.create(Security_Id=login,Society_Name=request.POST["Society_Name"],Citizen_Name=request.POST["Citizen_Name"],Guest_Name=request.POST["Guest_Name"],Reason_for_Comming=request.POST["Reason"],Contact=request.POST["Contect_No"],DateTime=request.POST["datetime"])
            
            messages.warning(request,"Entry Done")
    except:
        messages.warning(request,"Society Not Exist")
        return redirect(Guest_Entry_Page)                 

    return redirect(Guest_Entry_Page)
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    security=Security_Registration.objects.get(singup=login)
    Contaxt={
        "security":security
    }
    return render(request,Guest_entry_Page_Link,Contaxt)

def Entry_List(request):
    Guest_Entry_List_Page_Link
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    security=Security_Registration.objects.get(singup=login)
    guest_entry=Guest_Entry.objects.all()
    Contaxt={
        "security":security,
        "guest_entry":guest_entry,
    }
    return render(request,Guest_Entry_List_Page_Link,Contaxt)

def Security_Complain(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    security=Security_Registration.objects.get(singup=login)
    Contaxt={
        "security":security
    }
    return render(request,Make_Complain_Page_Link,Contaxt)

def Insert_Security_Complain(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    Type=Complain_Type.objects.get(Complain_Name=request.POST["Complain_type"])
    New_Complain=Complain.objects.create(Citizen_Id=login,Subject=request.POST["Subject"],Complain=Type,Entry_Date=request.POST["Entry_Date"])
    print(request.POST)
    print("Save")
    messages.warning(request,"Complain Registered ")

    return redirect(Security_Complain) 
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
                return redirect(Admin_Profile_Page)

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

""" def Load_Profile(request):
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
        return redirect(Login_Page) """

def Logout(request):
    print(request.session['Login_Name'])
    del request.session['Login_Name']
    return redirect(Login_Page)

def Registration_Validation(request):   
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
        
        if Role==['Committee']:
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
        elif login.Is_Admin:
            return redirect(Admin_Profile_Page)
       
    else:
        messages.warning(request,"Incorrect OTP")
        return redirect(OTP_Page)

    return redirect(OTP_Page)

def Change_Password_Of_Admin(request):
    try:
        login=SingUp.objects.get(Username=request.session['Login_Name'])
        
        if login.Password == request.POST["current_Password"]:
            
            if request.POST["new_password"] == request.POST["confirm_password"]:
                print(login.Password)
                login.Password = request.POST["new_password"]
                login.save()
                messages.warning(request,"Password Change Succssfully")
                return redirect(Admin_Account_Setting_Page)

                messages.warning(request,"Password Change")
                return redirect(Admin_Account_Setting_Page)

            else:
                messages.warning(request,"Both Password Not Match....")
                return redirect(Admin_Account_Setting_Page)
        else:
            messages.warning(request,"Invalid Password")
            return redirect(Admin_Account_Setting_Page)

        return redirect(Admin_Account_Setting_Page)
    except:
        pass

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
    security.society_name=request.POST["Society_Name"]
    security.save()

    return redirect(Login_Page)                                   

def Upload_Security_Image(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    security=Security_Registration.objects.get(singup=login)
    security.Security_Image=request.FILES["Security_Image"]
    security.save()
    print("Image Changed")
    return redirect(Security_Account_Setting_Page)

def Upload_Committee_Image(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    committee=Committee_Registration.objects.get(singup=login)
    committee.Committee_Image=request.FILES["Committee_Image"]
    committee.save()
    return redirect(Committee_Account_Setting)

def Upload_Citizen_Image(request):
    login=SingUp.objects.get(Username=request.session['Login_Name'])
    citizen=Citizen_Registration.objects.get(singup=login)
    citizen.Citizen_Image=request.FILES["Citizen_Image"]
    citizen.save()
    return redirect(Citizen_Account_Setting_Page)


#--------------------------------------------------------------------------------------------------------------                                      
                                            #End: Validation ...
                                 




