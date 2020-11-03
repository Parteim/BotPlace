from django.urls import path

from . import views

urlpatterns = [
    path('', views.vk_create_bot, name='vk'),
    path('get-vk-bot/<bot_slug>', views.get_vk_bot_instance, name='get-vk-bot'),
]