from django.shortcuts import render


def vk_create_bot(request):
    data = {
        'title': 'VK'
    }
    return render(request, 'vk/vk_page.html', data)
