from django import forms
from main.models import MailingSettings, Client, MailingAttempt, MailingMessage
from main.utils import StyleInputMixin


class MailingSettingsForm(StyleInputMixin, forms.ModelForm):
    class Meta:
        model = MailingSettings
        fields = ('sending_time', 'periodicity',)

    sending_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='Время рассылки')


class ClientUpdateForm(StyleInputMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ('full_name', 'email', 'comment',)


class MailingMessageForm(StyleInputMixin, forms.ModelForm):
    class Meta:
        model = MailingMessage
        fields = ('title', 'body',)


class MailingAttemptForm(StyleInputMixin, forms.ModelForm):
    class Meta:
        model = MailingAttempt
        fields = ('mailing_settings', 'clients', 'message',)
