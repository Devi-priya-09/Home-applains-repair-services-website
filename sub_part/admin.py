from django.contrib import admin
from .models import *

class customerregistertablesadmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'phone_number', 'address')

class CustomerBookingTableadmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'customer_email',
        'customer_door_number',
        'customer_address_street',
        'customer_address',
        'customer_phone_number',
        'home_appliance',
        'appliance_brand',
        'service_required',
        'issue_description',
        'date_of_order',
        'appliance_image',
        'extra_details',
        'created_at',
        'status',
        'treading',
        
    )

admin.site.register(customerregistertables, customerregistertablesadmin)
admin.site.register(CustomerBookingTable, CustomerBookingTableadmin)
