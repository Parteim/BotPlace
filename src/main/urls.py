from django.urls import path

from . import views

urlpatterns = [

    path('', views.sign_in_bot_place, name='login-Bot-Place'),
    path('sign-in', views.sign_in_bot_place, name='sign-in-Bot-Place'),

    path('sign-out', views.sign_out_bot_place, name='sign-out-Bot-Place'),

    path('sign-up', views.sign_up_bot_place, name='sign-up-Bot-Place'),
    path('create-bot-place', views.sign_up_bot_place, name='create-Bot-Place'),

    path('bot-place', views.bot_place, name='Bot-Place'),

    path('choosing-bot-for', views.choosing_bot_for, name='choosing-bot-for'),


    path('get-list-bots', views.get_list_bots, name='get-list-bots'),
]
