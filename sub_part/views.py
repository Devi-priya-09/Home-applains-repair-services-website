from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import *
import random
from django.db.models import Q

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

def user_login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def register_form_submission(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        otp_number = str(random.randint(100000, 999999)) 

        print(name, email, password, confirm_password, phone_number, address)

        # Check if email or phone number already exists
        if customerregistertables.objects.filter(email=email).exists():
            messages.error(request, "This email ID is already registered.", extra_tags='already')
            return render(request, 'register.html')
        elif customerregistertables.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "This phone number is already registered.", extra_tags='already')
            return render(request, 'register.html')
        
        # Save the new user record
        new_user = customerregistertables(
            name=name,
            email=email,
            password=password, 
            confirm_password=confirm_password, # Note: Passwords should be hashed using Django's authentication system
            phone_number=phone_number,
            address=address,
            otp_number=otp_number
         )
        new_user.save()

        # Generate and send OTP
      
        otp_number = str(random.randint(100000, 999999))  # Generate a 6-digit OTP

        subject = "Verify Your Account – OTP from SS HOME APPLAINS SERVICES Team"
        message = f"""
        Dear {name},

        Welcome to SS HOME APPLAINS SERVICES! To complete your registration and secure your account, please use the following One-Time Password (OTP):

        OTP: {otp_number}

        This OTP is valid for the next 10 minutes.
        Please do not share this code with anyone for security reasons.

        If you did not request this OTP, please ignore this email or contact our support team immediately at [Support Email/Phone Number].

        Thank you for choosing SS HOME APPLAINS SERVICES for your home appliance repair needs.

        Best regards,
        SS HOME APPLAINS SERIVES Team
        [Your Website] | [+91 8667023585]
        """

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
            messages.success(request, "Registration successful! Please check your email for OTP verification.")
            print("mail sent successfully")
        except Exception as e:
            messages.error(request, f"Error sending OTP email: {e}")
            print(f"mail not sent successfuly reason -> {e}")

        print("Data saved successfully")
        return render(request, 'login.html')

    return render(request, 'register.html')


def  login_page_submission(request):
   if customerregistertables.objects.filter(Q(otp_number=request.POST.get('otp_number')) | Q(email=request.POST.get('otp_number')),password=request.POST.get('password')).exists():
       print("login successfull")
       logger_data=customerregistertables.objects.get(Q(otp_number=request.POST.get('otp_number')) | Q(email=request.POST.get('otp_number')),password=request.POST.get('password'))
       print(f"{logger_data.name}")
    #    user_id=logger_data.id
    #    view_booking_details=CustomerBookingTable.objects.filter(customer_id=user_id)
       return render(request,'dashborad.html',{'logger_data':logger_data})
   else:
       print("login failed")
       messages.error(request,"invalid OTP number or password")
       return render(request,'login.html')



# View for user login


# View for registration (new user)

# View for user dashboard (after login)

def dashboard(request):
    return render(request, 'dashboard.html')

# View for service tracking

# def service_tracking(request, service_id):
#     # Get the service request
#     service = customerregistertables.objects.get(id=service_id, user=request.user)
#     return render(request, 'service_tracking.html', {'service': service})


def ac(request) :
    return render(request,'ac.html')  

def washing(request)    :
    return render(request,'washing.html')


def view_booking(request,)        :
    
     
    #  view_booking_details=CustomerBookingTable.objects.filter(customer_id=user_id)

     return render(request,'view_booking.html')
        
    

def book_order(request,user_id)   :
    print(f"user_id is{user_id}")
    logger_data=customerregistertables.objects.get(id=user_id)
       
    return render(request,'book_order.html',{'logger_data':logger_data}) 



def customer_booking_submission(request):
    if request.method == 'POST':
        # Make sure customer_id is not mistakenly assigned as a tuple (no comma at the end)
        customer_id = request.POST.get('customer_id')
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')

        # Handle file uploads (use request.FILES.get() for images)
        appliance_image = request.FILES.get('appliance_image')

        # Now ensure the correct indentation for the object creation
        customer_door_number = request.POST.get('customer_door_number')
        if not customer_door_number:
            messages.error(request, "Customer door number cannot be empty.")
            return render(request, 'book_order.html', {'logger_data': logger_data})

        ex1 = CustomerBookingTable(
            customer_id=customer_id,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_door_number=customer_door_number,
            customer_address_street=request.POST.get('customer_address_street'),
            customer_address=request.POST.get('customer_address'),
            customer_phone_number=request.POST.get('customer_phone_number'),
            home_appliance=request.POST.get('home_appliance'),
            appliance_brand=request.POST.get('appliance_brand'),
            service_required=request.POST.get('service_required'),
            issue_description=request.POST.get('issue_description'),
            date_of_order=request.POST.get('date_of_order'),
            appliance_image=appliance_image,  # Handling file upload
            extra_details=request.POST.get('extra_details'),
        )
        ex1.save()
        print("data shored successfully")
        logger_data = customerregistertables.objects.get(id=customer_id)
        return render(request, 'view_booking.html', {'logger_data': logger_data})



def view_booking_customer_details(request):
    pass


