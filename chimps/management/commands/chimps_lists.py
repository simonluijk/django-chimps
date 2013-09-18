from django.core.management.base import NoArgsCommand
from django.conf import settings
from mailsnake import MailSnake


class Command(NoArgsCommand):
    def handle_noargs(self, **kwargs):
        ms = MailSnake(getattr(settings, 'MAILCHIMP_KEY'))
        for lst in ms.lists()['data']:
            print('Name: {name}\nID: {id}\n'.format(**lst))
