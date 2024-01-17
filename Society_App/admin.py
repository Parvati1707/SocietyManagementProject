from django.contrib import admin
from .models import *
# Register your models here.
class HouseNo(admin.ModelAdmin):
  list_display = ("House_No","Society_Name")

class BlockNo(admin.ModelAdmin):
  list_display = ("Block_No","Society_Name")

admin.site.register(SingUp)
admin.site.register(Citizen_Registration)
admin.site.register(Committee_Registration)
admin.site.register(Security_Registration)
admin.site.register(Add_Society)
admin.site.register(Add_New_Block,BlockNo)
admin.site.register(Add_House,HouseNo)
admin.site.register(Arrange_Meeting)
