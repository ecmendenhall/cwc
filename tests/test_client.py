import unittest
import mock

from cwc.client import Client, Message


class TestClient(unittest.TestCase):

    def test_stores_api_key(self):
        client = Client(api_key='lolwutrofl')
        self.assertEqual(client.api_key, 'lolwutrofl')

    def test_stores_host(self):
        client = Client(host='https://fake-cwc.house.gov')
        self.assertEqual(client.host, 'https://fake-cwc.house.gov')

    def test_default_host_is_test_environment(self):
        client = Client()
        self.assertEqual(client.host, 'https://test-cwc.house.gov')

    def test_stores_delivery_agent(self):
        client = Client(delivery_agent={
            'name': 'Name',
            'ack_email': 'ack@example.com',
            'contact_name': 'Contact Name',
            'contact_email': 'contact@example.com',
            'contact_phone': '123-555-1234'
        })
        self.assertEqual(client.delivery_agent.name, 'Name')
        self.assertEqual(client.delivery_agent.ack_email, 'ack@example.com')
        self.assertEqual(client.delivery_agent.contact_name, 'Contact Name')
        self.assertEqual(client.delivery_agent.contact_email, 'contact@example.com')
        self.assertEqual(client.delivery_agent.contact_phone, '123-555-1234')

    @mock.patch('requests.post')
    def test_sends_message(self, mock_post):
        client = Client(api_key='lolwutrofl')
        client.send_message()
        mock_post.assert_called_with(
            'https://test-cwc.house.gov/v2/message',
            params={'apikey': 'lolwutrofl'}
        )

    @mock.patch('requests.post')
    def test_validates_message(self, mock_post):
        client = Client(api_key='lolwutrofl')
        client.validate_message()
        mock_post.assert_called_with(
            'https://test-cwc.house.gov/v2/validate',
            params={'apikey': 'lolwutrofl'}
        )
