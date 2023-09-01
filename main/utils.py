from django.http import HttpResponseForbidden
from django.urls import reverse_lazy


class OwnerMallingMixin:
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return HttpResponseForbidden()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class FormCreateMixin:
    template_name = 'main/pages/form_create.html'
    success_url = reverse_lazy('main:list_mailing')

    def form_valid(self, form):
        mailing_attempt = form.save(commit=False)
        mailing_attempt.user = self.request.user
        mailing_attempt.save()
        return super().form_valid(form)


class StyleInputMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
