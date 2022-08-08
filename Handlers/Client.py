import asyncio, aioschedule
from Keyboards import main_kb, unregistered_user_kb, profile_kb, water_kb, unregistered_user_kb_reg
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot
from DateBase import SqlLiteDb
from DateBase.users import Users
from DateBase.water import Water
from DateBase.DATABASE import session
from aiogram import types
from aiogram.dispatcher import Dispatcher


s = session()


class FSMregistr(StatesGroup):
    Nickname = State()


# start download or show profile
async def profile(message: types.Message):
    if message.chat.type == 'private':
        if s.query(Users.id).filter(Users.id == message.from_user.id).first():
            await bot.send_message(message.from_user.id, 'Choose a category:', reply_markup=profile_kb)
        else:
            await FSMregistr.Nickname.set()
            await message.answer('Enter your Name')


async def add_nickname(message: types.Message, state: FSMContext):
    id = message.from_user.id
    nick = message.text
    if message.from_user.username != None:
        tg_username = '@' + message.from_user.username
    else: tg_username = 'There is not'
    user = Users(id=id, nick=nick, tg_username=tg_username)
    await bot.send_message(message.from_user.id, 'Registration completed', reply_markup=main_kb)
    await state.finish()
    s.add(user)
    s.commit()
    s.close()


async def commands_start(message: types.Message):
    if message.chat.type == 'private':
        if s.query(Users.id).filter(Users.id == message.from_user.id).first():
            try:
                await bot.send_message(message.from_user.id, f'Hello, {message.from_user.first_name}', reply_markup=main_kb)
            except:
                await message.reply('Чтобы я смог с тобой общаться, напиши мне: https://web.telegram.org/z/#5258746451')
        else:
            await bot.send_message(message.from_user.id, f'Hello, {message.from_user.first_name}', reply_markup=unregistered_user_kb)


async def commands_help(message: types.Message):
    await bot.send_message(message.from_user.id, '''
    Список команд:
/Profile - ваш профиль
/Admin - профиль создателя Бота
/Water - контроль потребления воды
                                                    ''')


class FSMwater(StatesGroup):
    start = State()


async def water(message: types.Message, state: FSMContext):
    if s.query(Users.id).filter(Users.id == message.from_user.id).first() and not s.query(Water.users_id).filter(Water.users_id == message.from_user.id).first():
        await FSMwater.start.set()
        await message.answer('''Я могу контролировать потребление воды каждый день
Никакого спама, ты сам(а) пишешь когда выпил(а) стакан воды.
Чтобы начать - отправь "Yes"''')
    elif not s.query(Users.id).filter(Users.id == message.from_user.id).first():
        await bot.send_message(message.from_user.id, '''Я могу контролировать потребление воды каждый день
Никакого спама, ты сам(а) пишешь когда выпил(а) стакан воды.
Для этого вам нужно зарегистрироваться''', reply_markup=unregistered_user_kb_reg)
    elif s.query(Water).get(message.from_user.id).glass_of_water_today >= 8:
        await bot.send_message(message.from_user.id, f'You drank all {s.query(Water).get(message.from_user.id).glass_of_water_today} glasses that day', reply_markup=main_kb)
    else:
        await bot.send_message(message.from_user.id, f'Today you drank {s.query(Water).get(message.from_user.id).glass_of_water_today} glass of water. To meet the norm per day, you need {8 - s.query(Water).get(message.from_user.id).glass_of_water_today} more', reply_markup=water_kb)


async def status_water(message: types.Message, state: FSMContext):
        if message.text.lower() in ['"yes"', "'yes'", 'yes', 'да', '"да"', "'да'", '"da"', "'da'", 'da']:
            await bot.send_message(message.from_user.id, '''How to use:
You need to go to /PROFILE, then press /WATER. To add a drunk glass, you need to press /AddOne''', reply_markup=main_kb )
            water = Water(id=message.from_user.id, users_id=message.from_user.id)
            s.add(water)
            s.commit()
            s.close()
        await state.finish()


async def AddOne(message: types.Message):
    s.query(Water).get(message.from_user.id).glass_of_water_today += 1
    s.commit()
    s.close()
    if s.query(Water).get(message.from_user.id).glass_of_water_today >= 8:
        await bot.send_message(message.from_user.id, f'You drank all {s.query(Water).get(message.from_user.id).glass_of_water_today} glasses that day', reply_markup=main_kb)
    else: await bot.send_message(message.from_user.id,
                           f'Today you drank {s.query(Water).get(message.from_user.id).glass_of_water_today} glass of water. To meet the norm per day, you need {8 - s.query(Water).get(message.from_user.id).glass_of_water_today} more',
                           reply_markup=water_kb)


async def boys(message: types.Message):
    await SqlLiteDb.sql_read(message)


async def creator(message: types.Message):
    await bot.send_message(message.from_user.id, 'Admin: @sem4ek')
    if message.chat.type != 'private':
        await message.delete()


async def ok():
    for i in s.query(Water).all():
        s.query(Water).get(i.id).glass_of_water_today = 0
    s.commit()
    s.close()


async def data_null():
    aioschedule.every(1).day.at('21:00').do(ok)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(profile, commands=['Registration'])
    dp.register_message_handler(profile, commands=['profile'], state=None)
    dp.register_message_handler(add_nickname, state=FSMregistr.Nickname)
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(commands_help, commands=['Help'])
    dp.register_message_handler(water, commands=['water'], state=None)
    dp.register_message_handler(status_water, state=FSMwater.start)
    dp.register_message_handler(AddOne, commands=['AddOne'])
    dp.register_message_handler(boys, commands=['boys'])
    dp.register_message_handler(creator, commands=['admin'])