from rest_framework import serializers
from .models import *

class customer_booking_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBookingTable
        fields='__all__'