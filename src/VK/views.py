from django.shortcuts import render, redirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

import json

from .forms import VkBotFormCreation
from .models import VkBot


@login_required
def vk_create_bot(request):
    if request.method == 'POST':
        print(request.POST)
        form = VkBotFormCreation(request.POST)
        if form.is_valid():
            vk_bot = VkBot.objects.create_bot(
                bot_place=request.user,
                bot_name=request.POST['bot_name'],
                bot_for='vk',
                protection_key=request.POST['protection_key'],
                services_key_accessing=request.POST['services_key_accessing'],
                bot_id=request.POST['bot_id'],
            )
            print('vk bot created')
            return redirect('Bot-Place')

    data = {
        'title': 'Create vk bot',
        'form': VkBotFormCreation,
    }
    return render(request, 'vk/create_vk_bot.html', data)


@login_required
def get_vk_bot_instance(request, bot_slug):
    print(bot_slug)
    try:
        bot = VkBot.objects.get(bot_slug=bot_slug)
    except VkBot.DoesNotExist:
        print('does not exist')
        raise Http404('bot does not exist')
    print(bot.bot_place)
    print(request.user)
    if bot.bot_place != request.user:
        print('403')
        return HttpResponse(status=403, content_type="application/json")
    else:
        data = serialize('json', [bot])
        return HttpResponse(data, content_type="application/json")


@login_required
def update_vk_bot_instance(request, bot_slug):
    print(bot_slug)
    try:
        bot = VkBot.objects.get(bot_slug=bot_slug)
    except VkBot.DoesNotExist:
        print('does not exist')
        raise Http404('bot does not exist')
    if bot.bot_place != request.user:
        print('403')
        return HttpResponse(status=403, content_type="application/json")
    else:
        data = serialize('json', [bot])
        return HttpResponse(data, content_type="application/json")
