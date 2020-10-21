from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import BotPlace
from .forms import BotPlaceChangeForm, BotPlaceCreationForm


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
