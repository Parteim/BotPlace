from django.shortcuts import render

from .forms import VkBotFormCreation


def vk_create_bot(request):
    if request.method == 'POST':
        print(request.POST)
        form = VkBotFormCreation()
        if form.is_valid():
            form.save()
            print('vk bot created')
            return

    data = {
        'title': 'Create vk bot',
        'form': VkBotFormCreation,
    }
    return render(request, 'vk/create_vk_bot.html', data)
