from django.contrib import admin
from main.models import MailingAttempt, MailingSettings, MailingMessage
from users.models import User


@admin.register(MailingAttempt)
class MailingAttempt(admin.ModelAdmin):
    fields = ('client', 'mailing_settings', 'message', 'status',)


@admin.register(User)
class Client(admin.ModelAdmin):
    fields = ('email', 'full_name', 'comment',)


@admin.register(MailingSettings)
class MailingSettings(admin.ModelAdmin):
    fields = ('sending_time', 'periodicity', 'status',)


@admin.register(MailingMessage)
class MailingMessage(admin.ModelAdmin):
    fields = ('title', 'body',)
