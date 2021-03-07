import os
from aiogram import Bot, Dispatcher, types

from handlers.decorators import chat_is_group

API_TOKEN = os.environ.get('BOT_API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
@chat_is_group
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    answer = "Hi!\nI'm EchoBot! (for now)"
    await message.answer(answer)


@dp.message_handler()
@chat_is_group
async def echo(message: types.Message):
    """
    Echo function. Returns the same text user wrote.
    """

    answer = message.text
    await message.answer(answer)
