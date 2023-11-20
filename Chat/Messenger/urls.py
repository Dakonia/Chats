# ваш_проект/urls.py

from django.urls import path
from .views import index, chat, edit_profile, create_chat, join_chat

urlpatterns = [
    path('', index, name='index'),
    path('chat/<int:chat_id>/', chat, name='chat'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('create-chat/', create_chat, name='create_chat'),
    path('join-chat/<int:chat_id>/', join_chat, name='join_chat'),
    # Добавьте другие маршруты по мере необходимости
]