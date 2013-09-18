from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import SubscribeView


urlpatterns = patterns('',
    url(r'^subscribe/$', SubscribeView.as_view(),
        name='chimps_subscribe'),
    url(r'^subscribed/$',
        TemplateView.as_view(template_name='chimps/subscribed.html'),
        name='chimps_subscribed'),
)
