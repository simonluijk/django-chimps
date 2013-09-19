from django import template
from ..views import SubscribeView


register = template.Library()


@register.inclusion_tag('chimps/form.html')
def chimps_form():
    view = SubscribeView()
    return {'form': view.get_form_class()}
