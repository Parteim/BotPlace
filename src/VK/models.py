from django.db import models

from main.models import BaseBot


class VkBot(BaseBot):
    protection_key = models.CharField(max_length=255)
    services_key_accessing = models.CharField(max_length=255)

