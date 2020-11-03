from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

from .admin import BotPlaceCreationForm
from .forms import BotPlaceLogin
from .models import BaseBot


def sign_up_bot_place(request):
    if request.method == 'POST':
        form = BotPlaceCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign-in-Bot-Place')

    data = {
        'title': 'Sign up',
        'form': BotPlaceCreationForm,
        'form_title': 'Create Bot Place',
        'btn': 'Create',
    }

    return render(request, 'base/sign_up_bot_place.html', data)


def sign_in_bot_place(request):
    if request.user.is_authenticated:
        return redirect('Bot-Place')

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


@login_required
def bot_place(request):
    data = {
        'title': 'Bot place',
        'bots': BaseBot.objects.filter(bot_place=request.user),
    }
    return render(request, 'base/bot_place.html', data)


@login_required
def choosing_bot_for(request):
    data = {
        'title': 'Choosing bot for',
    }
    return render(request, 'base/choosing_bot_for.html', data)


@login_required
def get_list_bots(request):
    bots = BaseBot.objects.filter(bot_place=request.user)
    data = serialize('json', bots, cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type="application/json")
