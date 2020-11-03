from django.test import TestCase

import json

import requests


def run():
    response = requests.get(
        'http://127.0.0.1:8000/vk/get-vk-bot/B52F47',
    )

    try:
        response = response.json()
    except json.JSONDecodeError:
        return response

    return response


print(run())
