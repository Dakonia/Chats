# ваш_проект/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, Chat, Message

# @login_required
def index(request):
    all_chats = Chat.objects.all()
    context = {'all_chats': all_chats}
    return render(request, 'index.html', context)

# @login_required
def chat(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = Message.objects.filter(chat=chat)
    users = chat.users.all()

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(chat=chat, user=request.user, content=content)

    # Добавляем обработку выхода из чата
    if 'exit_chat' in request.POST:
        chat.users.remove(request.user)
        return redirect('index')

    context = {'chat': chat, 'messages': messages, 'users': users}
    return render(request, 'chat.html', context)

# @login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Обработка формы редактирования профиля
        new_name = request.POST.get('new_name')
        new_avatar = request.FILES.get('new_avatar')

        # Обновляем данные профиля
        user_profile.name = new_name
        if new_avatar:
            user_profile.avatar = new_avatar
        user_profile.save()

    context = {'user_profile': user_profile}
    return render(request, 'edit_profile.html', context)

# @login_required
def create_chat(request):
    if request.method == 'POST':
        chat_name = request.POST.get('chat_name')
        if chat_name and request.user.is_authenticated:
            new_chat = Chat.objects.create(name=chat_name)
            new_chat.users.add(request.user)
            return redirect('index')

    return render(request, 'create_chat.html')


# @login_required
def join_chat(request, chat_id):
    if request.user.is_authenticated:
        chat = get_object_or_404(Chat, id=chat_id)
        chat.users.add(request.user)
        chat.save()
        return redirect('chat', chat_id=chat.id)  # обновленный URL-путь
    return redirect('index')


