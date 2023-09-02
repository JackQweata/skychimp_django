from datetime import datetime
from django.db.models import Q
from main.models import MailingAttempt
from main.serives import send_mailing


def start_mailing():
    """ Рассылка """
    time_now = datetime.now().time()
    mailings = (MailingAttempt.objects.filter(mailing_settings__sending_time__lte=time_now) &
                MailingAttempt.objects.filter(~Q(mailing_settings__status='completed')))
    print(mailings)
    print(f'\n=========\n\nНачло рассылки\n{time_now}\n\n=========')
    for malling in mailings:
        send_mailing(malling)

