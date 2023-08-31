from main.models import MailingAttempt
from datetime import datetime, timedelta


def user_notifications(request):
    day_after_now = datetime.now() + timedelta(days=1)
    attempt = MailingAttempt.objects.filter(user=request.user, status='failure', timestamp__lte=day_after_now)

    return {'notifications': attempt}
