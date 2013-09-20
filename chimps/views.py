from django import forms
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.generic import FormView
from django.utils.translation import ugettext as _
from mailsnake import MailSnake


class SubscriptionForm(forms.Form):
    name = forms.CharField(_('Name'), max_length=100)
    email = forms.EmailField(_('Email'))


class SubscribeView(FormView):
    template_name = 'chimps/subscribe.html'
    form_class = SubscriptionForm

    def get_success_url(self):
        return reverse('chimps_subscribed')

    def form_valid(self, form):
        ms = MailSnake(getattr(settings, 'MAILCHIMP_KEY'))
        double_optin = getattr(settings, 'MAILCHIMP_CONFIRM', True)
        list_id = getattr(settings, 'MAILCHIMP_LIST_ID', None)

        if not list_id:
            list_id = ms.lists()['data'][0]['id']

        ms.listSubscribe(id=list_id, email_address=form.cleaned_data['email'],
                         merge_vars={'NAME': form.cleaned_data['name']},
                         update_existing=True, double_optin=double_optin)

        return super(SubscribeView, self).form_valid(form)
