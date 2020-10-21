from django.shortcuts import render

from .models import BotPlace, BotPlaceManager
from .admin import BotPlaceCreationForm


def index(request):
    data = {
        'title': 'Hi Bebra',
    }
    return render(request, 'base/index.html', data)


def sign_up_bot_place(request):
    if request.method == 'POST':
        form = BotPlaceCreationForm(request.POST)
        if form.is_valid():
            form.save()

    data = {
        'title': 'Sign in',
        'form': BotPlaceCreationForm,
    }

    return render(request, 'base/sign_up_bot_place.html', data)


def sign_in_bot_place(request):
    if request.method == 'POST':
        form = BotPlaceCreationForm(request.POST)
        if form.is_valid():
            form.save()

    data = {
        'title': 'Sign in',
        'form': BotPlaceCreationForm,
    }

    return render(request, 'base/sign_up_bot_place.html', data)
