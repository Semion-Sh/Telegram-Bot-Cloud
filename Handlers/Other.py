from aiogram import types
import json, string
from aiogram.dispatcher import Dispatcher
import asyncio, aioschedule
from kinds_of_poll import football_poll_rafieva
from aiogram.types import BotCommand
from .Client import english


bot_commands = [
    BotCommand('/admin', 'профиль создателя Бота'),
    BotCommand('/profile', 'твой профиль '),
]


async def mat_block(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()} \
            .intersection(set(json.load(open('cenz.json')))):
        name = message.from_user.first_name
        await message.answer(f'{name}, плохие слова запрещены!')
        await message.delete()


# football poll
async def spam_start():
    aioschedule.every().sunday.at('08:00').do(football_poll_rafieva)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(0)


async def english_spam_start():
    aioschedule.every().day.at('17:45').do(english)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(0)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(mat_block)