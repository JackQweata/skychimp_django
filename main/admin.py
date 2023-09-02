from django.contrib import admin
from main.models import MailingAttempt, MailingSettings, MailingMessage
from users.models import User

admin.site.register(MailingAttempt)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('is_active',)


@admin.register(MailingSettings)
class MailingSettings(admin.ModelAdmin):
    fields = ('status',)


@admin.register(MailingMessage)
class MailingMessage(admin.ModelAdmin):
    fields = ('title', 'body',)
