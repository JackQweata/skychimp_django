from main.models import MailingAttempt
from datetime import datetime, timedelta


def user_notifications(request):
    """ Уведомления """
    if not request.user.is_authenticated:
        return {'notifications': []}

    # day_after_now = datetime.now() + timedelta(days=1)
    logs = MailingAttempt.objects.filter(user=request.user)

    return {'notifications': logs}
