from aiogram import Bot, Dispatcher, types
import os


API_TOKEN = os.environ.get('BOT_API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

RESTRICTED_CHAT_TYPES = [
    types.ChatType.PRIVATE,
    types.ChatType.CHANNEL,
]


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    answer = 'You can only use this bot in group chats.'
    if message.chat.type not in RESTRICTED_CHAT_TYPES:
        answer = "Hi!\nI'm EchoBot! (for now)"
    await message.answer(answer)


@dp.message_handler()
async def echo(message: types.Message):
    """
    Echo function. Returns the same text user wrote.
    """

    answer = 'You can only use this bot in group chats.'
    if message.chat.type not in RESTRICTED_CHAT_TYPES:
        answer = message.text
    await message.answer(answer)
