from django.db import models

# Create your models here.
Resident_Choice=(
    ('owner','Owner'),
    ('tenant','Tenant')
)

Gender_choice=(
    ("m","Male"),
    ("f","Female")
)

class SingUp(models.Model):
    Username=models.CharField(max_length=50,default="",unique=True)
    Password=models.CharField(max_length=15,default="")
    Email=models.EmailField(default="",max_length=30)
    Is_Admin=models.BooleanField(default=False)
    Is_Citizen=models.BooleanField(default=False)
    Is_Committee=models.BooleanField(default=False)
    Is_Security=models.BooleanField(default=False)

    def __str__(self):
        return self.Username

class Citizen_Registration(models.Model):
    singup=models.ForeignKey(SingUp, on_delete=models.CASCADE)
    TotalMembers=models.CharField(max_length=50,default="")#
    BlockNo=models.CharField(max_length=10,default="")#
    HouseNo=models.CharField(max_length=10,default="")#
    Resident_Type=models.CharField(choices=Resident_Choice,max_length=20,default="")
    FirstName=models.CharField(max_length=20,default="")#
    LastName=models.CharField(max_length=20,default="")#
    #Email=models.EmailField(default="",max_length=30)
    BirthDate=models.DateField(auto_created=True,default="2018-12-12")
    Gender=models.CharField(choices=Gender_choice,max_length=20,default="")
    Profession=models.CharField(default="", max_length=50)
    AdharNumber=models.CharField(max_length=20,default="")#
    Contact=models.CharField(max_length=10,default="")#
    Contac2t=models.CharField(max_length=10,default="")#
    Address=models.TextField(default="",max_length=40)

    def __str__(self):
        return self.singup.Username

class Committee_Registration(models.Model):
    singup=models.ForeignKey(SingUp, on_delete=models.CASCADE)
    Contact=models.CharField(max_length=10,default="")
    #Email=models.EmailField(default="",max_length=30)
    BirthDate=models.DateField(auto_created=True,default="2018-12-12")
    Gender=models.CharField(choices=Gender_choice,max_length=20,default="")
    AdharNumber=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.singup.Username


class Security_Registration(models.Model):
    singup=models.ForeignKey(SingUp, on_delete=models.CASCADE)
    Contact=models.CharField(max_length=10,default="")
    #Email=models.EmailField(default="",max_length=30)
    BirthDate=models.DateField(auto_created=True,default="2018-12-12")
    Gender=models.CharField(choices=Gender_choice,max_length=20,default="")
    AdharNumber=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.singup.Username

          


#--------------------------------------------------------------------------------------------------------------
                                     
                                        #Start :Admin Related Tables

#--------------------------------------------------------------------------------------------------------------
class Add_Society(models.Model):
    Society_Name=models.CharField(default="",max_length=20,unique=True)
    Address=models.TextField(max_length=50)
    City=models.CharField(default="",max_length=100)
    PinCode=models.IntegerField(default="")
    No_Of_House=models.IntegerField(default="")
    Society_Image=models.ImageField(upload_to="static/Society_images", height_field=None, width_field=None, max_length=None)
    Entry_Date=models.DateField(auto_created=True,default="2018-12-12")

    def __str__(self):
        return self.Society_Name


class Add_New_Block(models.Model):
    Society_Name=models.ForeignKey(Add_Society, on_delete=models.CASCADE)
    Block_No=models.CharField(default="",max_length=50)
    NO_Of_Floors=models.IntegerField(default="")
    No_Of_Flats=models.IntegerField(default="")
    
    

House_Choice={
    ("1bhk","1BHK"),
    ("2bhk","2BHK"),
    ("3bhk","3BHK")
}

class Add_House(models.Model):
    Society_Name=models.ForeignKey(Add_Society, on_delete=models.CASCADE)
    House_No=models.IntegerField(default="")
    Block_No=models.ForeignKey(Add_New_Block, on_delete=models.CASCADE)
    House_Type=models.CharField(choices=House_Choice,max_length=50)
    Detail=models.TextField(default="")
    Image=models.ImageField(upload_to="static/Society_images", height_field=None, width_field=None, max_length=None)
    Entry_Date=models.DateField(auto_created=True,default="2018-12-12")

    

#--------------------------------------------------------------------------------------------------------------
                                     
                                        #End:Admin Related Tables

#--------------------------------------------------------------------------------------------------------------
   
class Fund_Type(models.Model):
    Fund_Name=models.CharField(default="", max_length=50)
    def __str__(self):
        return self.Fund_Name
    

class Raise_Fund(models.Model):
    Fund_Type=models.ForeignKey(Fund_Type, on_delete=models.CASCADE)
    DateTime=models.DateField(auto_created=True,default="2018-12-12")


class Arrange_Meeting(models.Model):
    Meet_Agenda=models.TextField(default="")
    DateTime=models.DateField(auto_created=True,default="2018-12-12")
    Meet_conclusion=models.TextField(default="")

    def __str__(self):
        return self.Meet_Agenda

class Notice_Type(models.Model):
    Notice_Name=models.CharField(default="", max_length=50)

    def __str__(self):
        return self.Notice_Name
    
class Notice(models.Model):
    Notice=models.ForeignKey(Notice_Type, on_delete=models.CASCADE)
    Subject=models.TextField(default="")
    DateTime=models.DateField(auto_created=True,default="2018-12-12")

    def __str__(self):
        return self.Notice
    
class Event_Type(models.Model):
    Event_Name=models.CharField(default="", max_length=50)

    def __str__(self):
        return self.Event_Name
    


class Society_Event(models.Model):
    Event_Type=models.ForeignKey(Event_Type, on_delete=models.CASCADE)
    DateTime=models.DateField(auto_created=True,default="2018-12-12")

    def __str__(self):
        return self.Event_Name
    
    
#--------------------------------------------------------------------------------------------------------------
                                     
                                        #Start:Citizen Related Tables

#--------------------------------------------------------------------------------------------------------------

class Complain_Type(models.Model):
    Complain_Name=models.CharField(default="", max_length=50)

    def __str__(self):
        return self.Complain_Name
    
class Complain(models.Model):
    Citizen_Id=models.ForeignKey(SingUp, on_delete=models.CASCADE)
    Subject=models.TextField(default="")
    Relpay=models.TextField(default="")
    Status=models.CharField(default="Pending", max_length=50)
    Entry_Date=models.DateField(auto_created=True,default="2018-12-12")
    Complain=models.ForeignKey(Complain_Type, on_delete=models.CASCADE)
    

class Sell_House(models.Model):
    House_Id=models.ForeignKey(Add_House, on_delete=models.CASCADE)
    Society_Id=models.ForeignKey(Add_Society, on_delete=models.CASCADE)
    Citizen_Id=models.ForeignKey(SingUp, on_delete=models.CASCADE)
    Sell_Price=models.FloatField(default="",max_length=10)
    Entry_Date=models.DateField(auto_created=True,default="2018-12-12")
    

    
class Rent_House(models.Model):
    House_Id=models.ForeignKey(Add_House, on_delete=models.CASCADE)
    Society_Id=models.ForeignKey(Add_Society, on_delete=models.CASCADE)
    Citizen_Id=models.ForeignKey(SingUp, on_delete=models.CASCADE)
    Rent_Price=models.FloatField(default="",max_length=20)
    Entry_Date=models.DateField(auto_created=True,default="2018-12-12")


class Personal_Event_Booking(models.Model):
    House_Id=models.ForeignKey(Add_House, on_delete=models.CASCADE)
    Society_Id=models.ForeignKey(Add_Society, on_delete=models.CASCADE)
    Citizen_Id=models.ForeignKey(SingUp, on_delete=models.CASCADE)
    Event_Name=models.CharField(default="",max_length=50)
    No_Of_Guest=models.IntegerField(default="")
    Entry_Date=models.DateField(auto_created=True,default="2018-12-12")
    

#--------------------------------------------------------------------------------------------------------------
                                     
                                        #End:Citizen Related Tables

#--------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------
                                     
                                        #Start:Security Related Tables

#--------------------------------------------------------------------------------------------------------------


class Guest_Entry(models.Model):
    Security_Id=models.ForeignKey(SingUp, on_delete=models.CASCADE)
    Citizen_Name=models.ForeignKey(Citizen_Registration, on_delete=models.CASCADE)
    Guest_Name=models.CharField(default="",max_length=50)
    Reason_for_Comming=models.TextField(default="")
    Contact=models.CharField(default="", max_length=50)
    DateTime=models.DateField(auto_created=True,default="2018-12-12")

    def __str__(self):
        return self.Guest_Name
    


#--------------------------------------------------------------------------------------------------------------
                                     
                                        #End:Security Related Tables

#--------------------------------------------------------------------------------------------------------------
