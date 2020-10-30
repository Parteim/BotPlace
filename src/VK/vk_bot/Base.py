import requests


class VkBotInstance:
    def __init__(self, access_token, version_api='5.124'):
        self.access_token = access_token
        self.version_api = version_api


class BaseVkBot:
    def __init__(self, bot):
        self.bot_id = None
        self.access_token = bot.access_token
        self.version_api = bot.version_api
        self.url = 'https://api.vk.com/method/'

    def get(self, method, **kwargs):
        params = {
            'v': self.version_api,
            'access_token': self.access_token,
        }

        params.update(kwargs)

        response = requests.get(
            url=self.url + method,
            params=params,
        )
        return response

    def post(self, url, data=None, json=None, **kwargs):
        response = requests.post(
            url,
            data,
            json,
        )
        return response
