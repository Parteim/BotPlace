import requests


class BaseVkBot:
    def __init__(self, version_api='5.124'):
        self.bot_id = None
        self.access_token = '2949bad42949bad42949bad4122924d73c229492949bad474ec05c908e127c920034d67'
        self.version_api = version_api
        self.url = 'https://api.vk.com/method/'

    def get(self, method, **kwargs):
        params = {
            'v': self.version_api,
            'access_token': self.access_token,
        }

        params.update(kwargs)

        response = requests.get(
            url=self.url+method,
            params=params,
        )
        return response.json()

    def post(self, url, data=None, json=None, **kwargs):
        response = requests.post(
            url,
            data,
            json,
        )
        return response.json()
