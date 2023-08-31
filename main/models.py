from django.db import models

from users.models import User

MAILING_PERIOD_CHOICES = (
    ('daily', 'Раз в день'),
    ('weekly', 'Раз в неделю'),
    ('monthly', 'Раз в месяц'),
)

STATUS_CHOICES = (
        ('success', 'Успешно'),
        ('failure', 'Неудачно'),
)

STATUS_SETTINGS = (
    ('created', 'Создан'),
    ('completed', 'завершена'),
    ('launched', 'запущена'),
)


class Client(models.Model):
    full_name = models.CharField('ФИО', max_length=100)
    email = models.EmailField('Email клиента')
    comment = models.TextField('Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.full_name} -> {self.email}'


class MailingSettings(models.Model):
    sending_time = models.TimeField(verbose_name='время рассылки')
    periodicity = models.CharField(max_length=100, verbose_name='периодичность', choices=MAILING_PERIOD_CHOICES)
    status = models.CharField(max_length=20, default='created', choices=STATUS_SETTINGS, verbose_name='Статус')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sending_time} -> {self.periodicity}'

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'


class MailingMessage(models.Model):
    title = models.CharField(max_length=200, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class MailingAttempt(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='время последней попытки')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='статус попытки')
    server_response = models.TextField(blank=True, null=True, verbose_name='ответ почтового сервера', default='Все ок')

    mailing_settings = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='Настройка')
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')
    message = models.ForeignKey(MailingMessage, on_delete=models.CASCADE, verbose_name='Письмо')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.message} -> {self.mailing_settings}"

    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'
