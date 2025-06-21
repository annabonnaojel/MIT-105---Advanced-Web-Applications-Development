# trainer/utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_expired_notice(email, trainer_name, certificate_name, validity_date):
    subject = f"Reminder: '{certificate_name}' Certificate Expiring Soon"
    message = (
        f"Dear {trainer_name},\n\n"
        f"Your certificate for '{certificate_name}' is set to expire on {validity_date}.\n"
        "Please take the necessary steps to renew it.\n\n"
        "Thank you,\nTESDA Office"
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
