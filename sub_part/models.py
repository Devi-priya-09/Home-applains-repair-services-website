from django.db import models
import datetime
import os
from django.core.exceptions import ValidationError

# Function to generate unique file names based on current timestamp
def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime("%y%m%d%H:%M:%S")
    new_filename = "%s_%s"%(now_time, filename)
    return os.path.join("uploads/", new_filename)


# Customer Registration Model
class customerregistertables(models.Model):  # Class name in PascalCase
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    otp_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # String representation of the model


# Customer Booking Model
class CustomerBookingTable(models.Model):  # Class name in PascalCase
    customer_id=models.CharField(max_length=500)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_door_number = models.CharField(max_length=100)
    customer_address_street = models.CharField(max_length=100)
    customer_address = models.TextField(max_length=500)
    customer_phone_number = models.CharField(max_length=100)
    home_appliance = models.CharField(max_length=500, help_text="e.g., AC, Washing Machine")
    appliance_brand = models.CharField(max_length=100)

    INSTALLATION_CHOICES = [
        ('Installation', 'Install'),
        ('Maintenance', 'Maintenance'),
        ('Repair', 'Home Appliances Repair services')
    ]
    service_required = models.CharField(max_length=50, choices=INSTALLATION_CHOICES, default='Repair')

    issue_description = models.TextField(max_length=500,null=False,blank=False)
    date_of_order = models.DateField()

    appliance_image = models.ImageField(upload_to=getFileName, blank=True, null=True)  # Corrected field to use getFileName

    extra_details = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=100, default="Pending")
    treading=models.BooleanField(default=False,help_text="0-default,1-treading")



class Feedback(models.Model):  # ✅ Renamed from add_feedback to Feedback
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='feedback_images', null=True, blank=True)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.rating < 1 or self.rating > 5:
            raise ValidationError('Rating must be between 1 and 5.')

    def __str__(self):
        return self.name
