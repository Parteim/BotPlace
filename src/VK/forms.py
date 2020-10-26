from django import forms
from django.core.exceptions import ValidationError

from .models import VkBot


class VkBotFormCreation(forms.ModelForm):
    bot_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'id': 'email',
            'class': 'bot_name_field vk_bot_field',
            'name': 'bot_name',
            'placeholder': 'Bot name',
        }
    ))

    class Meta:
        model = VkBot
        fields = ('bot_name',)
