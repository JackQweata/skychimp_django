import smtplib

from django.core.mail import send_mail
from config import settings
from main.models import LogServers


def send_mail_service(title: str, body: str, email_list: list):
    res_email = send_mail(title, body, settings.EMAIL_HOST_USER, email_list, fail_silently=True)
    return res_email


def send_mailing(attempt):
    server_response = {'failure': [], 'success': []}

    attempt.mailing_settings.status = 'launched'
    attempt.save()

    try:
        for item in attempt.clients.all():
            try:
                send_mail(attempt.message.title, attempt.message.body,
                          settings.EMAIL_HOST_USER, [item.email], fail_silently=True)

                server_response['success'].append(item.email)

            except smtplib.SMTPException as _err:
                server_response['failure'].append(item.email)
                continue

        for key, value in server_response.items():
            for item in value:
                log = LogServers.objects.create(status=key, server_response=item, user=attempt.user)
                attempt.logs.add(log)

        attempt.mailing_settings.status = 'created'
        attempt.save()

    except Exception as _err:
        print(f'Error: {_err}')
