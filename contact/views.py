from django.views.generic.edit import FormView
from .models import ContactRequest
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.contrib import messages


class ContactView(FormView):
    model = ContactRequest
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = '/contact/'
    success_message = 'Your message has been sent.'

    def form_valid(self, form):
        email = EmailMessage(
            form.cleaned_data.get('name'),
            form.cleaned_data.get('content'),
            form.cleaned_data.get('email'),
            ['szymon.korzonek@gmail.com'],
            reply_to=[form.cleaned_data.get('email')])
        email.send()
        form.save()
        messages.success(self.request, self.success_message)
        return super(ContactView, self).form_valid(form)
