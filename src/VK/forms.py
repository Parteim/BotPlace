from django import forms

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
    protection_key = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'id': 'protection_key',
            'class': 'bot_name_field vk_bot_field',
            'name': 'protection_key',
            'placeholder': 'Protection key',
        }
    ))
    services_key_accessing = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'id': 'services_key_accessing',
            'class': 'bot_name_field vk_bot_field',
            'name': 'services_key_accessing',
            'placeholder': 'Services key of accessing',
        }
    ))

    bot_id = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'id': 'services_key_accessing',
            'class': 'bot_name_field vk_bot_field',
            'name': 'bot_id',
            'placeholder': 'Application id',
        }
    ))

    class Meta:
        model = VkBot
        fields = ('bot_name', 'protection_key', 'services_key_accessing', 'bot_id',)
