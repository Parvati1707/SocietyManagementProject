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


admin.site.register(Fund_Type)
admin.site.register(Raise_Fund)
admin.site.register(Notice_Type)
admin.site.register(Notice)
admin.site.register(Event_Type)
admin.site.register(Society_Event)
admin.site.register(Arrange_Meeting)


admin.site.register(Sell_House)
admin.site.register(Rent_House)
admin.site.register(Personal_Event_Booking)
admin.site.register(Complain_Type)
admin.site.register(Complain)

admin.site.register(Guest_Entry)

