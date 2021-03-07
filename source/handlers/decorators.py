from aiogram import types

RESTRICTED_CHAT_TYPES = [
    types.ChatType.PRIVATE,
    types.ChatType.CHANNEL,
]
ONLY_GROUPS_MESSAGE = 'You can only use this bot in group chats.'


def chat_is_group(func):
    def wrapper(message: types.Message):
        if message.chat.type in RESTRICTED_CHAT_TYPES:
            return message.answer(ONLY_GROUPS_MESSAGE)
        return func(message)
    return wrapper
