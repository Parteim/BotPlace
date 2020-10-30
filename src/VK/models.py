from django.db import models
import uuid

from main.models import BaseBot


class VkBotManager(models.Manager):
    def create_bot(self, bot_place, bot_name, bot_for, bot_id, protection_key, services_key_accessing):
        bot_slug = uuid.uuid4().hex[:6].upper()
        bot = self.model(
            bot_place=bot_place,
            bot_name=bot_name,
            bot_slug=bot_slug,
            bot_for=bot_for,
            bot_id=bot_id,
            protection_key=protection_key,
            services_key_accessing=services_key_accessing,
        )

        bot.save()

        return bot


class VkBot(BaseBot):
    bot_id = models.IntegerField()
    protection_key = models.CharField(max_length=255)
    services_key_accessing = models.CharField(max_length=255)

    objects = VkBotManager()

    REQUIRED_FIELDS = [
        'bot_id',
        'protection_key',
        'services_key_accessing',
    ]
