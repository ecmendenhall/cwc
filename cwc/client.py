import requests
from collections import namedtuple, defaultdict


DeliveryAgent = namedtuple(
    'DeliveryAgent',
    [
        'name',
        'ack_email',
        'contact_name',
        'contact_email',
        'contact_phone'
    ]
)
DeliveryAgent.__new__.__defaults__ = (None,) * len(DeliveryAgent._fields)


class Client:

    def __init__(
            self,
            api_key=None,
            host='https://test-cwc.house.gov',
            delivery_agent={}
    ):
        self.api_key = api_key
        self.host = host
        self.delivery_agent = DeliveryAgent(**delivery_agent)

    def send_message(self):
        self._post('message')

    def validate_message(self):
        self._post('validate')

    def _post(self, action):
        requests.post(self.host + '/v2/' + action, params={'apikey': self.api_key})
