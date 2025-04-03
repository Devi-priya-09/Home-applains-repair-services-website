from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

def send_seasonal_offer_email(recipient_email, name, offer_type):
    """
    Sends an email notification for seasonal offers based on predefined schedules.
    """
    current_month = datetime.now().month

    # Define email sending rules
    if offer_type == "summer" and current_month in [3, 4, 5, 6, 7]:  # March to July
        subject = "🌞 Summer Special Offer – SS HOME APPLIANCES SERVICES"
        message = f"""
        Dear {name},

        We have an exciting seasonal offer just for you at SS HOME APPLIANCES SERVICES!  

        🌞 Summer Special Offer:
        Book your appliance repair now and get 20% off!  
        Hurry, this offer is valid until July 31st.  

        📅 Advance Booking Discount: 
        Plan ahead and save! Get 15% off when you book your service at least 2 weeks in advance**.  

        Don't miss out on these limited-time deals. Schedule your service today and enjoy hassle-free appliance repairs at unbeatable prices!  

        For any queries, contact us at devipriyagod1@gmail.com / 📞8667023585.  

        Best regards,  
        SS HOME APPLIANCES SERVICES Team  
        FIXIT.com  
        📞+91 8667023585
        """
    elif offer_type == "winter" and current_month in [11, 12, 1, 2]:  # November to February
        subject = "❄️ Winter Special Offer – SS HOME APPLIANCES SERVICES"
        message = f"""
        Dear {name},

        Stay warm this winter with our exclusive appliance repair discounts!  

        ❄️ Winter Special Offer:
        Get 15% off on heating appliance repairs this season.  
        Offer valid until February 28th.  

        Don't let winter breakdowns ruin your comfort! Book your repair service now and save big.  

        For any queries, contact us at devipriyagod1@gmail.com / 📞8667023585.  

        Best regards,  
        SS HOME APPLIANCES SERVICES Team  
        FIXIT.com  
        📞+91 8667023585
        """
    else:
        return  # Do not send an email if it's outside the seasonal period

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [recipient_email],
        fail_silently=False,
    )
