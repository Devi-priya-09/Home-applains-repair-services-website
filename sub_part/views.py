from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import *
import random
from django.db.models import Q

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .utils import send_seasonal_offer_email  
from rest_framework import generics
from .serializers import customer_booking_data_serializer

# list and create books
# convert all data into API
class CustomerListBookingCreateView(generics.ListCreateAPIView):
    queryset=CustomerBookingTable.objects.all()
    serializer_class=customer_booking_data_serializer


# retrive,update,delete a book  single data
# convert single data into ApI(can update,delete)
class CustomerRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView)   :
    queryset=CustomerBookingTable.objects.all() 
    serializer_class=customer_booking_data_serializer

    



def index(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'feedbacks': feedbacks})

def add_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = int(request.POST.get('rating', 0))
        text = request.POST.get('text')
        image = request.FILES.get('image')

        # Check if feedback already exists for this email
        if Feedback.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', 'message': 'You have already submitted feedback.'})

        feedback = Feedback.objects.create(name=name, email=email, rating=rating, text=text, image=image)
        image_url = feedback.image.url if feedback.image else ''

        return JsonResponse({
            'status': 'success',
            'name': feedback.name,
            'rating': feedback.rating,
            'text': feedback.text,
            'image_url': image_url,
        })
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def delete_feedback(request, feedback_id):
    if request.method == 'POST':
        feedback = get_object_or_404(Feedback, id=feedback_id)
        feedback.delete()
        return JsonResponse({'status': 'success', 'message': 'Feedback deleted successfully'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

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
        otp_number = str(random.randint(100000, 999999))  # Generate OTP once

        print(name, email, password, confirm_password, phone_number, address)

        if customerregistertables.objects.filter(email=email).exists():
            messages.error(request, "This email ID is already registered.", extra_tags='already')
            return render(request, 'register.html')
        elif customerregistertables.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "This phone number is already registered.", extra_tags='already')
            return render(request, 'register.html')

        new_user = customerregistertables(
            name=name,
            email=email,
            password=password,
            confirm_password=confirm_password,
            phone_number=phone_number,
            address=address,
            otp_number=otp_number
        )
        new_user.save()

        subject = "Verify Your Account – OTP from SS HOME APPLIANCES SERVICES Team"
        message = f"""
        Dear {name},

        Welcome to SS HOME APPLIANCES SERVICES! To complete your registration and secure your account, please use the following One-Time Password (OTP):

        OTP: {otp_number}

        This OTP is valid for the next 10 minutes.
        Please do not share this code with anyone for security reasons.

        If you did not request this OTP, please ignore this email or contact our support team immediately at [Support Email/Phone Number].

        Thank you for choosing SS HOME APPLIANCES SERVICES for your home appliance repair needs.

        Best regards,
        SS HOME APPLIANCES SERVICES Team
        [Your Website] | [+91 8667023585]
        """

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
            messages.success(request, "Registration successful! Please check your email for OTP verification.")
            print("Mail sent successfully")
        except Exception as e:
            messages.error(request, f"Error sending OTP email: {e}")
            print(f"Mail not sent successfully. Reason -> {e}")

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





def dashboard(request, user_id):
    try:
        logger_data = customerregistertables.objects.get(id=user_id)
        return render(request, 'dashboard.html', {'logger_data': logger_data})
    except customerregistertables.DoesNotExist:
       
        messages.error(request, "User not found!")
        return redirect('index')  






# def service_tracking(request, service_id):
#     # Get the service request
#     service = customerregistertables.objects.get(id=service_id, user=request.user)
#     return render(request, 'service_tracking.html', {'service': service})


def ac(request) :
    return render(request,'ac.html')  

def washing(request)    :
    return render(request,'washing.html')


def view_booking(request, user_id):
    print(f"user_id is {user_id}")
    
    logger_data = customerregistertables.objects.get(id=user_id)
    view_booking_details = CustomerBookingTable.objects.filter(customer_id=user_id)
    return render(request, 'view_booking.html', {
        'logger_data': logger_data,
        'view_booking_details': view_booking_details
    })


    

def book_order(request,user_id)  :
    print(f"user_id is{user_id}")
    logger_data=customerregistertables.objects.get(id=user_id)
    messages.success(request,"your booking is successfully booked to check to view table")  
    return render(request,'book_order.html',{'logger_data':logger_data}) 



def customer_booking_submission(request):
    if request.method == 'POST':
       
        customer_id = request.POST.get('customer_id')
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        appliance_image = request.FILES.get('appliance_image')


        ex1 = CustomerBookingTable(
            customer_id=customer_id,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_door_number=request.POST.get('customer_door_number'),
            customer_address_street=request.POST.get('customer_address_street'),
            customer_address=request.POST.get('customer_address'),
            customer_phone_number=request.POST.get('customer_phone_number'),
            home_appliance=request.POST.get('home_appliance'),
            appliance_brand=request.POST.get('appliance_brand'),
            service_required=request.POST.get('service_required'),
            issue_description=request.POST.get('issue_description'),
            date_of_order=request.POST.get('date_of_order'),
            appliance_image=appliance_image,
            extra_details=request.POST.get('extra_details'),
        )
        ex1.save()
        print("Data stored successfully")

       
        return redirect('view_booking', user_id=customer_id)

    return render(request, 'book_order.html')



def view_booking_customer_details(request):
    pass







def send_offer_email_view(request):
    recipient_email = request.GET.get("email")
    name = request.GET.get("name", "Customer")  
    offer_type = request.GET.get("offer_type", "summer")  

    if not recipient_email:
        return JsonResponse({"error": "Email parameter is required!"}, status=400)

    send_seasonal_offer_email(recipient_email, name, offer_type)
    return JsonResponse({"message": f"Offer email ({offer_type}) sent to {recipient_email}!"})

def test_email(request):
    try:
        send_mail(
            'Test Email',
            'This is a test email.',
            settings.EMAIL_HOST_USER,
            ['recipient@example.com'],  # Replace with a valid recipient email
        )
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error sending email: {e}")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


def feedback(request):
    return render(request,'feedback.html')