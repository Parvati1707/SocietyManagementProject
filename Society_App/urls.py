from django.urls import path
from .views import *

urlpatterns = [
                                        # Page Urls
    path('',Index),
    path("Login_Page",Login_Page,name="Login_Page"),
    path("Registration_Page",Registration_Page,name="Registration_Page"),
    path("Forgate_Password_Page",Forgate_Password_Page,name="Forgate_Password_Page"),
    path("OTP_Page",OTP_Page,name="OTP_Page"),
    path("Citizen_Registration_Page",Citizen_Registration_Page,name="Citizen_Registration_Page"),
    path("Committee_Registration_Page",Committee_Registration_Page,name="Committee_Registration_Page"),
    path("Security_Registration_Page",Security_Registration_Page,name="Security_Registration_Page"),
    path("Citizen_Profile_Page",Citizen_Profile_Page,name="Citizen_Profile_Page"),
    path("Committee_Profile_Page",Committee_Profile_Page,name="Committee_Profile_Page"),
    path("Security_Profile_Page",Security_Profile_Page,name="Security_Profile_Page"),

                                        # Admin Related Urls

    path("Admin_Profile_Page",Admin_Profile_Page,name="Admin_Profile_Page"),

    path("Admin_Account_Setting_Page",Admin_Account_Setting_Page,name="Admin_Account_Setting_Page"),
    path("Update_Admin_Profile",Update_Admin_Profile,name="Update_Admin_Profile"),

    path("Add_Society_Page",Add_Society_Page,name="Add_Society_Page"),
    path("Add_New_Society",Add_New_Society,name="Add_New_Society"),

    path("Add_New_Block_Page",Add_New_Block_Page,name="Add_New_Block_Page"),
    path("Add_Block",Add_Block,name="Add_Block"),

    path("Add_Houses_Page",Add_Houses_Page,name="Add_Houses_Page"),
    path("Add_house",Add_house,name="Add_house"),

    path("Manage_Complain_Page",Manage_Complain_Page,name="Manage_Complain_Page"),

    path("Report_Page",Report_Page,name="Report_Page"),
    path("Sell_Rent_List_Page",Sell_Rent_List_Page,name="Sell_Rent_List_Page"),
    
                                       #  Citizen Related Urls
    path("Citizen_Account_Setting_Page",Citizen_Account_Setting_Page,name="Citizen_Account_Setting_Page"),
    path("Update_citizen_Profile",Update_citizen_Profile,name="Update_citizen_Profile"),


    path("Rent_House_Page",Rent_House_Page,name="Rent_House_Page"),
    path("Insert_Rent_House",Insert_Rent_House,name="Insert_Rent_House"),


    path("Sell_House_Page",Sell_House_Page,name="Sell_House_Page"),
    path("Insert_Sell_House",Insert_Sell_House,name="Insert_Sell_House"),

    path("Citizen_Complain",Citizen_Complain,name="Citizen_Complain"),

    path("Booking_Request_Page",Booking_Request_Page,name="Booking_Request_Page"),

                                       #  Committee Related Urls

    path("Committee_Account_Setting",Committee_Account_Setting,name="Committee_Account_Setting"),
    path("Update_Committee_Profile",Update_Committee_Profile,name="Update_Committee_Profile"),

    path("Arrange_Meeting",Arrange_Meeting,name="Arrange_Meeting"),

    path("Raise_fund_Request_Page",Raise_fund_Request_Page,name="Raise_fund_Request_Page"),

    path("Add_Notice_Page",Add_Notice_Page,name="Add_Notice_Page"),

    path("Add_Event_Page",Add_Event_Page,name="Add_Event_Page"),

                                       #  Security Related Urls

    path("Security_Account_Setting_Page",Security_Account_Setting_Page,name="Security_Account_Setting_Page"),
    path("Update_Security_Profile",Update_Security_Profile,name="Update_Security_Profile"),

    path("Guest_Entry_Page",Guest_Entry_Page,name="Guest_Entry_Page"),

    path("Security_Complain",Security_Complain,name="Security_Complain"),

                                       #  Validations Urls
                                    
    path("Arrange_Meeting",Arrange_Meeting,name="Arrange_Meeting"),                                
    path("Logout",Logout,name="Logout"),
    path("Login_Validation",Login_Validation,name="Login_Validation"),
    path("Registration_Validation",Registration_Validation,name="Registration_Validation"),
    path("Citizen_Validation",Citizen_Validation,name="Citizen_Validation"),
    path("Committee_Validation",Committee_Validation,name="Committee_Validation"),
    path("Security_Validation",Security_Validation,name="Security_Validation"),
    path("Forgate_Password_Validation",Forgate_Password_Validation,name="Forgate_Password_Validation"),
    path("OTP_varification",OTP_varification,name="OTP_varification"),
    path("Change_Password_Of_Citizen",Change_Password_Of_Citizen,name="Change_Password_Of_Citizen"),
    path("Change_Password_Of_Security",Change_Password_Of_Security,name="Change_Password_Of_Security"),
    path("Change_Password_Of_Committee",Change_Password_Of_Committee,name="Change_Password_Of_Committee"),
    path("Change_Password_Of_Admin",Change_Password_Of_Admin,name="Change_Password_Of_Admin"),
    
]
