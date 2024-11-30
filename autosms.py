import random
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDiscussionMessageRequest

# Укажите свои данные
api_id = '25377105'  # Ваш API ID из Telegram
api_hash = '603b3cf4af53834a3e871f96da405e65'  # Ваш API Hash из Telegram

# Список каналов (можно добавить несколько каналов)
channels = [
    '@qweasxdac',  # Юзернейм или ID первого канала
]

# Список сообщений для отправки
comments = [
    "Не могу поверить, что такое действительно происходит…😨",
    "Это просто кошмар!😱",
    "Что-то тут точно не так…🫣",
    "Жутко, не могу оторвать взгляд.😳",
    "Это даже не укладывается в голове…👀",
    "Страшно до ужаса, надеюсь, всё закончится хорошо…😟",
    "Никогда не думала, что увижу нечто подобное…😧",
    "Не могу перестать думать об этом…😔",
    "Как такое вообще возможно?!😵‍💫",
    "Это просто ужас! Прямо до мурашек.🫣",
    "Трепет в теле после того, что только что увидела…😬",
    "Не могу поверить, что мир стал таким…😢",
    "Кошмар, даже не знаю, что и сказать.😣",
    "Сильно не по себе от этого…😞",
    "Это выходит за рамки всего, что я ожидала увидеть.😯",
    "Я в шоке… как такое возможно?!😳",
    "Не могу поверить, что это реальность…😔",
    "Мурашки по коже… не могу даже дышать от страха.😶‍🌫️",
    "Это не для слабонервных…😱",
    "Как такое вообще могло случиться? Просто ужас!😨",
]

# Инициализация клиента
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=channels))  # Обрабатываем новые сообщения из каналов
async def handler(event):
    try:
        # Проверяем, связан ли пост с чатом обсуждений
        discussion = await client(GetDiscussionMessageRequest(
            peer=event.message.peer_id,
            msg_id=event.message.id
        ))

        # Если у поста есть обсуждения, отправляем комментарий в чат обсуждений
        if discussion.messages and discussion.messages[0].peer_id.channel_id:
            discussion_chat = discussion.messages[0].peer_id  # Получаем привязанный чат обсуждений
            random_comment = random.choice(comments)  # Выбираем случайный комментарий
            await client.send_message(discussion_chat, random_comment, reply_to=discussion.messages[0].id)
            print(f"Комментарий '{random_comment}' оставлен в разделе комментариев к посту {event.message.id}")
        else:
            print(f"У поста {event.message.id} нет обсуждений.")
    except Exception as e:
        print(f"Ошибка: {e}")

print("Скрипт запущен...")
with client:
    client.run_until_disconnected()
