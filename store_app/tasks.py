from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_message(recipient_list, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email="admin@mail.com",
        recipient_list=recipient_list,
    )
    return f"Сообщение {message} отправлено на почту {recipient_list}"
