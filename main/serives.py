from datetime import datetime
from django.core.mail import send_mail
from config import settings
import pytz


def send_mail_service(title: str, body: str, email_list: list):
    res_email = send_mail(title, body, settings.EMAIL_HOST_USER, email_list, fail_silently=True)
    return res_email


def send_mailing(attempt):
    timezone = pytz.timezone('Europe/Moscow')
    server_response = []

    attempt.mailing_settings.status = 'launched'
    attempt.save()
    attempt.status = 'success'

    try:
        for item in attempt.clients.all():
            res_email = send_mail(attempt.message.title, attempt.message.body,
                                  settings.EMAIL_HOST_USER, [item.email], fail_silently=True)

            if not res_email:
                attempt.status = 'failure'
                server_response.append(f'Ошибка отправка клиенту {item.email}')
                continue

            server_response.append(f'Успешно отправлено {item.email}')

        attempt.server_response = '\n'.join(server_response)
        attempt.timestamp = datetime.now(timezone)
        attempt.mailing_settings.status = 'completed'
        attempt.save()

    except Exception as _err:
        print(f'Error: {_err}')
