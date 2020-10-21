from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import BotPlace


class BotPlaceCreationForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={
            'id': 'email',
            'class': 'create_bot_place_input',
            'name': 'email',
            'placeholder': 'email',
        }
    ))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'id': 'password',
            'class': 'create_bot_place_input',
            'name': 'password',
            'placeholder': 'password',
        }
    ))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'id': 'confirm_password',
            'class': 'create_bot_place_input',
            'name': 'confirm_password',
            'placeholder': 'password',
        }
    ))

    class Meta:
        model = BotPlace
        fields = ('email',)

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            return ValidationError('Incorrect password')
        return confirm_password

    def save(self, commit=True):
        bot_place = super().save(commit=False)
        bot_place.set_password(self.cleaned_data['password'])
        if commit:
            bot_place.save()
        return bot_place


class BotPlaceChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = BotPlace
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class BotPlaceLogin(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={
            'id': 'email',
            'class': 'login_bot_place_input',
            'name': 'email',
            'placeholder': 'email',
        }
    ))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'id': 'password',
            'class': 'login_bot_place_input',
            'name': 'password',
            'placeholder': 'password',
        }
    ))

    class Meta:
        model = BotPlace
        fields = ('email',)
