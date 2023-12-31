# Generated by Django 4.2.4 on 2023-09-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='Email клиента')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='LogServers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('success', 'Успешно'), ('failure', 'Неудачно')], max_length=10, verbose_name='статус попытки')),
                ('server_response', models.TextField(blank=True, default='Все ок', null=True, verbose_name='ответ почтового сервера')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='время последней попытки')),
            ],
        ),
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='тема письма')),
                ('body', models.TextField(verbose_name='тело письма')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sending_time', models.TimeField(verbose_name='время рассылки')),
                ('periodicity', models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], max_length=100, verbose_name='периодичность')),
                ('status', models.CharField(choices=[('created', 'Создан'), ('completed', 'Завершена'), ('launched', 'Запущена')], default='created', max_length=20, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
