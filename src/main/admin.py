from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
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


class BotPlaceAdmin(BaseUserAdmin):
    form = BotPlaceChangeForm
    add_form = BotPlaceCreationForm

    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'confirm_password'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(BotPlace, BotPlaceAdmin)
admin.site.unregister(Group)