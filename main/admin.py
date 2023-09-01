from django.contrib import admin
from main.models import MailingAttempt, MailingSettings, MailingMessage
from users.models import User

admin.site.register(MailingAttempt)

admin.site.register(User)


@admin.register(MailingSettings)
class MailingSettings(admin.ModelAdmin):
    fields = ('sending_time', 'periodicity', 'status',)


@admin.register(MailingMessage)
class MailingMessage(admin.ModelAdmin):
    fields = ('title', 'body',)
