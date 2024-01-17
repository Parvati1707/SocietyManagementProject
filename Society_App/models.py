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
    BirthDate=models.DateField(auto_created=True,default="2018-12-12")
    Gender=models.CharField(choices=Gender_choice,max_length=20,default="")
    AdharNumber=models.CharField(max_length=20,default="")#
    Contact=models.CharField(max_length=10,default="")#
    Contac2t=models.CharField(max_length=10,default="")#
    Address=models.TextField(default="",max_length=40)

    def __str__(self):
        return self.singup.Username

class Committee_Registration(models.Model):
    singup=models.ForeignKey(SingUp, on_delete=models.CASCADE)
    Contact=models.CharField(max_length=10,default="")
    BirthDate=models.DateField(auto_created=True,default="2018-12-12")
    Gender=models.CharField(choices=Gender_choice,max_length=20,default="")
    AdharNumber=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.singup.Username


class Security_Registration(models.Model):
    singup=models.ForeignKey(SingUp, on_delete=models.CASCADE)
    Contact=models.CharField(max_length=10,default="")
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
    NoHouse=models.IntegerField(default="")
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
    House_No=models.IntegerField(default=100)
    Block_No=models.ForeignKey(Add_New_Block, on_delete=models.CASCADE)
    House_Type=models.CharField(choices=House_Choice,max_length=50)
    Detail=models.TextField(default="")
    Image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    Entry_Date=models.DateField(auto_created=True,default="2018-12-12")

    

#--------------------------------------------------------------------------------------------------------------
                                     
                                        #End:Admin Related Tables

#--------------------------------------------------------------------------------------------------------------
   

class Arrange_Meeting(models.Model):
    Meet_Agenda=models.TextField(default=True)
    DateTime=models.DateField(auto_created=True,default="2018-12-12")
    Meet_conclusion=models.TextField(default="")





    