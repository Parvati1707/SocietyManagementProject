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
    Email=models.EmailField(default="",max_length=30)#
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
    BirthDate=models.DateField(auto_created=True,default="1980-12-11")
    Gender=models.CharField(choices=Gender_choice,max_length=20,default="")
    AdharNumber=models.CharField(max_length=20,default="")#
    #Email=models.EmailField(default="",max_length=30)#
    Profession=models.CharField(max_length=50,default="")#
    Contact=models.CharField(max_length=10,default="")#
    Contac2t=models.CharField(max_length=10,default="")#
    Address=models.CharField(max_length=40,default="")#

    def __str__(self):
        return self.singup.Username

class Committee_Registration(models.Model):
    singup=models.ForeignKey(SingUp, on_delete=models.CASCADE)
    #Email=models.EmailField(default="",max_length=30)
    Contact=models.CharField(max_length=10,default="")
    BirthDate=models.DateField(auto_created=True,default="1980-12-11")
    Gender=models.CharField(choices=Gender_choice,max_length=20,default="")
    AdharNumber=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.singup.Username


class Security_Registration(models.Model):
    singup=models.ForeignKey(SingUp, on_delete=models.CASCADE)
    #Email=models.EmailField(default="",max_length=30)
    Contact=models.CharField(max_length=10,default="")
    BirthDate=models.DateField(auto_created=True,default="1980-12-11")
    Gender=models.CharField(choices=Gender_choice,max_length=20,default="")
    AdharNumber=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.singup.Username



    





    