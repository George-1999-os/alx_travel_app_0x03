# listings/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_email(user_email, booking_details):
    subject = 'Booking Confirmation'
    message = f'Your booking is confirmed: {booking_details}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])
