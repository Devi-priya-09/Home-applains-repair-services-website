from django.contrib import admin
from .models import *
# Register your models here.
class customerregistertablesadmin(admin.ModelAdmin):
    list_display=('name','email','password','phone_number','address')

class CustomerBookingTableadmin(admin.ModelAdmin):
    list_display2=('customer_name','customer_email','customer_Door_Number','customer_address_street','customer_address','customer_Phone_number','home_appliance','appliance_brand','service_required','issue_description','date_of_order','appliance_image','extra_details')

admin.site.register(customerregistertables,customerregistertablesadmin)
admin.site.register(CustomerBookingTable,CustomerBookingTableadmin)
