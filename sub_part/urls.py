from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),  # Updated to match the form action
    path('register', views.register, name='register'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('register_form_submission', views.register_form_submission, name='register_form_submission'),
    path('login_page_submission', views.login_page_submission, name='login_page_submission'),
    path('ac', views.ac, name='ac'),
    path('washing', views.washing, name='washing'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('view_booking', views.view_booking, name='view_booking'),
    path('book_order/<int:user_id>', views.book_order, name='book_order'),
    path('customer_booking_submission', views.customer_booking_submission, name='customer_booking_submission'),
]