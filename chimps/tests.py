from mock import patch, Mock
from django.test import TestCase
from django.test.client import RequestFactory

from chimps.views import SubscribeView


class ViewTestCase(TestCase):
    def test_view_calls_api_correctly(self):
        """
        Test MailSnake api is called on successfull subscription.
        """

        data = {'name': 'Test Name', 'email': 'test@example.com'}
        request = RequestFactory().post('', data=data)
        view = SubscribeView.as_view()
        mc_api = Mock()

        with patch('chimps.views.MailSnake') as mocked_snake:
            mocked_snake.return_value = mc_api
            view(request)

            kwargs = {
                'double_optin': True,
                'merge_vars': {'NAME': 'Test Name'},
                'email_address': 'test@example.com',
                'id': 'test-mailchimp-list-id',
                'update_existing': True
            }
            mc_api.listSubscribe.assert_called_with(**kwargs)
