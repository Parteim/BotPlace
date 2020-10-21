from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('sign_in', views.sign_up_bot_place, name='auth'),
    path('', views.sign_up_bot_place, name='auth'),
]