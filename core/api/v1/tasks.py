# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
import redis

@shared_task
def send_password_reset_email(email):
    token = get_random_string(length=32)
    r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASSWORD, db=0)
    r.setex(token, 600, email)
    subject = 'Password Reset'
    message = f'Use this token to reset your password: {token}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
