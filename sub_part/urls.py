from django.urls import path
from . import views
from .views import send_offer_email_view

from .views import CustomerListBookingCreateView,CustomerRetriveUpdateDestroyView
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('register_form_submission', views.register_form_submission, name='register_form_submission'),
    path('login_page_submission', views.login_page_submission, name='login_page_submission'),
    path('ac', views.ac, name='ac'),
    path('washing', views.washing, name='washing'),
    path('dashboard/<int:user_id>/', views.dashboard, name='dashboard'),
    path('view_booking/<int:user_id>', views.view_booking, name='view_booking'),
    path('book_order/<int:user_id>', views.book_order, name='book_order'),
    path('customer_booking_submission', views.customer_booking_submission, name='customer_booking_submission'),
    path('customer_full_data/',CustomerListBookingCreateView.as_view(), name='customer_full_data'),
    path('customer_single_data/<int:pk>/',CustomerRetriveUpdateDestroyView.as_view(),name="customer_single_data"),

    path('send-offer-email/', send_offer_email_view, name='send_offer_email'),

]

