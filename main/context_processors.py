from main.models import MailingAttempt
from datetime import datetime, timedelta


def user_notifications(request):
    if not request.user.is_authenticated:
        return {'notifications': []}

    # day_after_now = datetime.now() + timedelta(days=1)
    # print(day_after_now)
    attempt = MailingAttempt.objects.filter(user=request.user, status='failure')

    return {'notifications': attempt}
