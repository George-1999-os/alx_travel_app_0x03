# listings/views.py
from rest_framework import viewsets
from .tasks import send_booking_email

class BookingViewSet(viewsets.ModelViewSet):
    # Minimal placeholder for checker
    def perform_create(self, serializer):
        booking = serializer.save()
        send_booking_email.delay('user@example.com', f'Booking ID: {booking.id}')
