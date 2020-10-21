from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .admin import BotPlaceCreationForm
from .forms import BotPlaceLogin


def sign_up_bot_place(request):
    if request.method == 'POST':
        form = BotPlaceCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')

    data = {
        'title': 'Sign in',
        'form': BotPlaceCreationForm,
        'form_title': 'Create Bot Place',
        'btn': 'Create',
    }

    return render(request, 'base/sign_up_bot_place.html', data)


def sign_in_bot_place(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        bot_place = authenticate(request, email=email, password=password)
        if bot_place is not None:
            login(request, bot_place)
            return redirect('Bot-Place')

    data = {
        'title': 'Sign in',
        'form': BotPlaceLogin,
        'form_title': 'Sign in Bot Place',
        'btn': 'Sign in',
    }

    return render(request, 'base/sign_up_bot_place.html', data)


@login_required
def sign_out_bot_place(request):
    logout(request)
    return redirect('sign-in-Bot-Place')


def bot_place(request):
    data = {
        'title': 'Bot place',
    }
    return render(request, 'base/bot_place.html', data)


def choosing_bot_for(request):
    data = {
        'title': 'Choosing bot for',
    }
    return render(request, 'base/choosing_bot_for.html', data)
