from django.urls import path
from main.apps import MainConfig
from main.views import *
from django.contrib.auth.decorators import login_required

app_name = MainConfig.name

urlpatterns = [
    path('', login_required(Index.as_view()), name='home'),
    path('create_mailing/', login_required(MailingAttemptListView.as_view()), name='list_mailing'),

    path('create_settings/', login_required(MailingSettingsCreateView.as_view()), name='create_settings'),
    path('delete_settings/<int:pk>/', login_required(MailingSettingsDeleteView.as_view()), name='delete_settings'),
    path('edit_settings/<int:pk>/', login_required(MailingSettingsUpdateView.as_view()), name='edit_settings'),

    path('create_client/', login_required(ClientCreateView.as_view()), name='create_client'),
    path('delete_client/<int:pk>/', login_required(ClientDeleteView.as_view()), name='delete_client'),
    path('edit_client/<int:pk>/', login_required(ClientUpdateView.as_view()), name='edit_client'),

    path('create_message/', login_required(MailingMessageCreateView.as_view()), name='create_message'),
    path('delete_message/<int:pk>', login_required(MailingMessageDeleteView.as_view()), name='delete_message'),
    path('edit_message/<int:pk>', login_required(MailingMessageUpdateView.as_view()), name='edit_message'),

    path('create_task/', login_required(MailingAttemptCreateView.as_view()), name='create_task'),
    path('edit_task/<int:pk>/', login_required(MailingAttemptUpdateView.as_view()), name='update_task'),
    path('detail_task/<int:pk>/', login_required(MailingAttemptDetailView.as_view()), name='detail_task'),
    path('delete_task/<int:pk>/', login_required(MailingAttemptDeleteView.as_view()), name='delete_task'),
]
