from django.test import TestCase

import requests


def run():
    response = requests.get(
        'http://127.0.0.1:8000/get-list-bots'
    )

    data = None
    return data


if __name__ == '__main__':
    run()
