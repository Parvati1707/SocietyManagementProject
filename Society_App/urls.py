from django.urls import path
from .views import *

urlpatterns = [
                                        # Page Urls
    path('',Index),
    path("Login_Page",Login_Page,name="Login_Page"),
    path("Registration_Page",Registration_Page,name="Registration_Page"),
    path("Forgate_Password_Page",Forgate_Password_Page,name="Forgate_Password_Page"),
    path("Citizen_Registration_Page",Citizen_Registration_Page,name="Citizen_Registration_Page"),
    path("Committee_Registration_Page",Committee_Registration_Page,name="Committee_Registration_Page"),
    path("Security_Registration_Page",Security_Registration_Page,name="Security_Registration_Page"),
    path("Citizen_Profile_Page",Citizen_Profile_Page,name="Citizen_Profile_Page"),
    path("Committee_Profile_Page",Committee_Profile_Page,name="Committee_Profile_Page"),
    path("Security_Profile_Page",Security_Profile_Page,name="Security_Profile_Page"),

                                       #  Validations Urls

    path("Login_Validation",Login_Validation,name="Login_Validation"),
    path("Registration_Validation",Registration_Validation,name="Registration_Validation"),
    path("Citizen_Validation",Citizen_Validation,name="Citizen_Validation"),
    path("Committee_Validation",Committee_Validation,name="Committee_Validation"),
    path("Security_Validation",Security_Validation,name="Security_Validation"),
]
