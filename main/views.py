from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from main.forms import MailingSettingsForm, ClientUpdateForm, MailingAttemptForm, MailingMessageForm
from main.models import MailingAttempt, MailingMessage, MailingSettings, Client
from main.serives import send_mailing, send_mail_service
from users.models import User


class Index(ListView):
    model = MailingAttempt
    template_name = 'main/pages/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        self.object = super().get_context_data(**kwargs)
        self.object['users'] = len(User.objects.all())
        self.object['messages'] = len(MailingMessage.objects.all())
        return self.object


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


class MailingSettingsCreateView(CreateView):
    form_class = MailingSettingsForm
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')

    def form_valid(self, form):
        mailing_attempt = form.save(commit=False)
        mailing_attempt.user = self.request.user
        mailing_attempt.save()
        return super().form_valid(form)


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    template_name = 'main/pages/form_delete.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    fields = ('sending_time', 'periodicity', 'status',)
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')


class ClientCreateView(CreateView):
    form_class = ClientUpdateForm
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')

    def form_valid(self, form):
        mailing_attempt = form.save(commit=False)
        mailing_attempt.user = self.request.user
        mailing_attempt.save()
        return super().form_valid(form)


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'main/pages/form_delete.html'
    success_url = reverse_lazy('main:list_mailing')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientUpdateForm
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingMessageCreateView(CreateView):
    form_class = MailingMessageForm
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')

    def form_valid(self, form):
        mailing_attempt = form.save(commit=False)
        mailing_attempt.user = self.request.user
        mailing_attempt.save()
        return super().form_valid(form)


class MailingMessageDeleteView(DeleteView):
    model = MailingMessage
    template_name = 'main/pages/form_delete.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingMessageUpdateView(UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingAttemptCreateView(CreateView):
    form_class = MailingAttemptForm
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')

    def form_valid(self, form):
        mailing_attempt = form.save(commit=False)
        mailing_attempt.user = self.request.user
        mailing_attempt.save()
        return super().form_valid(form)


class MailingAttemptUpdateView(UpdateView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingAttemptDeleteView(DeleteView):
    model = MailingAttempt
    template_name = 'main/pages/form_delete.html'
    success_url = reverse_lazy('main:list_mailing')


class MailingAttemptDetailView(DetailView):
    model = MailingAttempt
    template_name = 'main/pages/attempt_detail.html'
    success_url = reverse_lazy('main:list_mailing')
