from django import forms
from main.models import MailingSettings, Client, MailingAttempt, MailingMessage


class MailingSettingsForm(forms.ModelForm):
    class Meta:
        model = MailingSettings
        fields = ('sending_time', 'periodicity',)

    sending_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='Время рассылки')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('full_name', 'email', 'comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingMessageForm(forms.ModelForm):
    class Meta:
        model = MailingMessage
        fields = ('title', 'body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingAttemptForm(forms.ModelForm):
    class Meta:
        model = MailingAttempt
        fields = ('mailing_settings', 'clients', 'message',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
