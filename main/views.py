import json

from django.http import HttpResponseForbidden, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from main.forms import MailingSettingsForm, ClientUpdateForm, MailingAttemptForm, MailingMessageForm
from main.models import MailingAttempt, MailingMessage, MailingSettings, Client
from main.serives import send_mailing
from main.utils import FormCreateMixin, OwnerMallingMixin
from users.models import User


class Index(ListView):
    model = MailingAttempt
    template_name = 'main/pages/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        self.object = super().get_context_data(**kwargs)
        self.object['users'] = len(User.objects.all())
        self.object['messages'] = len(MailingMessage.objects.all())
        return self.object


class MailingSettingsCreateView(FormCreateMixin, CreateView):
    form_class = MailingSettingsForm


class MailingSettingsDeleteView(OwnerMallingMixin, DeleteView):
    model = MailingSettings
    template_name = 'main/pages/form_delete.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingSettingsUpdateView(OwnerMallingMixin, UpdateView):
    model = MailingSettings
    fields = ('sending_time', 'periodicity', 'status',)
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')


class ClientCreateView(FormCreateMixin, CreateView):
    form_class = ClientUpdateForm


class ClientDeleteView(OwnerMallingMixin, DeleteView):
    model = Client
    template_name = 'main/pages/form_delete.html'
    success_url = reverse_lazy('main:list_mailing')


class ClientUpdateView(OwnerMallingMixin, UpdateView):
    model = Client
    form_class = ClientUpdateForm
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingMessageCreateView(FormCreateMixin, CreateView):
    form_class = MailingMessageForm


class MailingMessageDeleteView(OwnerMallingMixin, DeleteView):
    model = MailingMessage
    template_name = 'main/pages/form_delete.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingMessageUpdateView(OwnerMallingMixin, UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingAttemptCreateView(FormCreateMixin, CreateView):
    form_class = MailingAttemptForm


class MailingAttemptUpdateView(OwnerMallingMixin, UpdateView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingAttemptDeleteView(OwnerMallingMixin, DeleteView):
    model = MailingAttempt
    template_name = 'main/pages/form_delete.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingAttemptDetailView(OwnerMallingMixin, DetailView):
    model = MailingAttempt
    template_name = 'main/pages/attempt_detail.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingAttemptListView(ListView):
    model = MailingAttempt
    template_name = 'main/pages/create_mailing.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user).order_by('-pk')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['mailing_settings'] = MailingSettings.objects.filter(user=self.request.user)
        context['clients'] = Client.objects.filter(user=self.request.user)
        context['messages'] = MailingMessage.objects.filter(user=self.request.user)
        return context


def req_start_milling(request):
    data = json.loads(request.body.decode('utf-8'))

    milling = MailingAttempt.objects.get(pk=data.get('pk'))
    if not milling:
        return JsonResponse({'message': 'пул не найден'})

    if milling.user != request.user:
        return JsonResponse({'message': 'Ошибка доступа'})

    send_mailing(milling)

    return JsonResponse({'status': 'ok'})
