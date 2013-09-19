# Django-Chimps

**Allow users to subscribe to MailChimp email lists.**

# Overview

Django-Chimps provides forms and views to allow users to subscribe to MailChimp emailing lists.

# Requirements

* Python
* Django
* mailsnake (1.6.2)

# Installation

Install using `pip`...

    pip install django-chimps

Add `'chimps'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'chimps',
    )

Set `MAILCHIMP_KEY` in your settings.

    MAILCHIMP_KEY = '###'

Run `python manage.py chimp_lists` to get a list of mailing lists. Then set `MAILCHIMP_LIST_ID` in your settings.

Include `chimps.urls` in your urlpatterns.

    url(r'^chimps/', include('chimps.urls')),


If you which to have a form on each page, add this to your base template.

    {% load chimp_tags %}

    {% block mailchimp_form %}
        {% chimps_form %}
    {% endblock %}

That's it, we're done!
