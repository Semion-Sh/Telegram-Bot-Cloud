from aiogram import types
import json, string
from aiogram.dispatcher import Dispatcher
import asyncio, aioschedule
from kinds_of_poll import football_poll_rafieva
from aiogram.types import BotCommand


bot_commands = [
    BotCommand('/admin', 'профиль создателя Бота'),
]

d = {
    'а': ['а', 'a', '@'],
    'б': ['б', '6', 'b'],
    'в': ['в', 'b', 'v'],
    'г': ['г', 'r', 'g'],
    'д': ['д', 'd', 'g'],
    'е': ['е', 'e'],
    'ё': ['ё', 'e'],
    'ж': ['ж', 'zh'],
    'з': ['з', 'z'],
    'и': ['и', 'u', 'i'],
    'й': ['й', 'u', 'i'],
    'к': ['к', 'k', 'i{', '|{'],
    'л': ['л', 'l', 'ji'],
    'м': ['м', 'm'],
    'н': ['н', 'h', 'n'],
    'о': ['о', 'o', '0'],
    'п': ['п', 'n', 'p'],
    'р': ['р', 'r', 'p'],
    'с': ['с', 'c', 's'],
    'т': ['т', 'm', 't'],
    'у': ['у', 'y', 'u'],
    'ф': ['ф', 'f'],
    'х': ['х', 'x', 'h', '}{'],
    'ц': ['ц', 'c', 'u,'],
    'ч': ['ч', 'ch'],
    'ш': ['ш', 'sh'],
    'щ': ['щ', 'sch'],
    'ь': ['ь', 'b'],
    'ы': ['ы', 'bi'],
    'ъ': ['ъ'],
    'э': ['э', 'e'],
    'ю': ['ю', 'io'],
    'я': ['я', 'ya']
}


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


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(mat_block)