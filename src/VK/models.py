from django.db import models

from main.models import BotPlace


class VkBot(models.Model):
    bot_place = models.ForeignKey(BotPlace, on_delete=models.CASCADE)

    bot_name = models.CharField(max_length=100)

    unique_bot_id = models.CharField(max_length=20, unique=True)

    protection_key = models.CharField(max_length=255)
    services_key_accessing = models.CharField(max_length=255)

    def __str__(self):
        return f'<name: {self.bot_name}; id: {self.unique_bot_id}>'
