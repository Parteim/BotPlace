from django.test import TestCase

import requests
import time
from threading import Thread


def run():
    i = 0
    while i < 100:
        i += 1
        print(i)
        time.sleep(1)
    return


if __name__ == '__main__':
    thread1 = Thread(target=run, args=())
    thread2 = Thread(target=run, args=())

    thread1.start()
    thread2.start()