from django.shortcuts import render, redirect

from .forms import VkBotFormCreation
from .models import VkBot


def vk_create_bot(request):
    if request.method == 'POST':
        print(request.POST)
        form = VkBotFormCreation(request.POST)
        if form.is_valid():
            vk_bot = VkBot.objects.create_bot(
                bot_place=request.user,
                bot_name=request.POST['bot_name'],
                bot_for='vk',
            )
            print('vk bot created')
            return redirect('Bot-Place')

    data = {
        'title': 'Create vk bot',
        'form': VkBotFormCreation,
    }
    return render(request, 'vk/create_vk_bot.html', data)
