import asyncio, aioschedule
from Keyboards import main_kb, unregistered_user_kb, profile_kb, water_kb, unregistered_user_kb_reg, workout_kb, push_ups_kb, bars_kb, pull_ups_kb
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot
from DateBase import SqlLiteDb
from DateBase.users import Users
from DateBase.water import Water
from DateBase.workout import Workout
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
Send "Yes" to start''')
    elif not s.query(Users.id).filter(Users.id == message.from_user.id).first():
        await bot.send_message(message.from_user.id, '''Я могу контролировать потребление воды каждый день
Никакого спама, ты сам(а) пишешь когда выпил(а) стакан воды.
Для этого вам нужно зарегистрироваться''', reply_markup=unregistered_user_kb_reg)
    elif s.query(Water).get(message.from_user.id).glass_of_water_today >= 8:
        await bot.send_message(message.from_user.id, f'You drank all {s.query(Water).get(message.from_user.id).glass_of_water_today} glasses that day', reply_markup=main_kb)
    else:
        await bot.send_message(message.from_user.id, f'Today you drank {s.query(Water).get(message.from_user.id).glass_of_water_today} out of 8 glass of water', reply_markup=water_kb)

# {8 - s.query(Water).get(message.from_user.id).glass_of_water_today}

async def status_water(message: types.Message, state: FSMContext):
        if message.text.lower() in ['"yes"', "'yes'", 'yes', 'да', '"да"', "'да'", '"da"', "'da'", 'da']:
            await bot.send_message(message.from_user.id, '''How to use:
You need to go to /PROFILE, then press /WATER. To add a drunk glass, you need to press /AddOne''', reply_markup=water_kb )
            water = Water(id=message.from_user.id, users_id=message.from_user.id, tg_name='@' + message.from_user.username)
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
                           f'Today you drank {s.query(Water).get(message.from_user.id).glass_of_water_today} glass of water out of 8',
                           reply_markup=water_kb)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------
class FSMworkout(StatesGroup):
    start = State()


class FSMpush_ups(StatesGroup):
    push_ups = State()


class FSMbars(StatesGroup):
    bars = State()


class FSMpull_ups(StatesGroup):
    pull_ups = State()


async def workout_w(message: types.Message, state: FSMContext):
    if s.query(Users.id).filter(Users.id == message.from_user.id).first() and not s.query(Workout.users_id).filter(Workout.users_id == message.from_user.id).first():
        await FSMworkout.start.set()
        await message.answer('''Write to me how much you did Push ups, Bars, Pull ups, I will add it to workout for the day
Send "Yes" to start''', reply_markup=main_kb)
    elif not s.query(Users.id).filter(Users.id == message.from_user.id).first():
        await bot.send_message(message.from_user.id, 'Please register', reply_markup=unregistered_user_kb_reg)
    else:
        await bot.send_message(message.from_user.id, f'Choose an exercise category:', reply_markup=workout_kb)


async def status_workout(message: types.Message, state: FSMContext):
    if message.text.lower() in ['"yes"', "'yes'", 'yes', 'да', '"да"', "'да'", '"da"', "'da'", 'da']:
        await bot.send_message(message.from_user.id, '''How to use:
You need to go to /PROFILE, then press /WORKOUT and choose a category''', reply_markup=main_kb)
        workout = Workout(id=message.from_user.id, users_id=message.from_user.id, tg_name='@' + message.from_user.username)
        s.add(workout)
        s.commit()
        s.close()
    await state.finish()


async def push_ups(message: types.Message):
    if s.query(Users.id).filter(Users.id == message.from_user.id).first() and not s.query(Workout.users_id).filter(Workout.users_id == message.from_user.id).first():
        await message.answer('Write to me how much you did push-ups, I will add it to pushups for the day')
    elif not s.query(Users.id).filter(Users.id == message.from_user.id).first():
        await bot.send_message(message.from_user.id, 'Please register', reply_markup=unregistered_user_kb_reg)
    else:
        await bot.send_message(message.from_user.id, f'Today you did {s.query(Workout).get(message.from_user.id).push_ups_today} push-ups', reply_markup=push_ups_kb)


async def Add_push_ups(message: types.Message):
    await FSMpush_ups.push_ups.set()
    await message.answer('Enter the number of pushups:')


async def save_push_ups(message: types.Message,  state: FSMContext):
    s.query(Workout).get(message.from_user.id).push_ups_today += int(message.text)
    s.query(Workout).get(message.from_user.id).push_ups_all += int(message.text)
    s.commit()
    s.close()
    await state.finish()
    await bot.send_message(message.from_user.id,
                           f'Today you did {s.query(Workout).get(message.from_user.id).push_ups_today} push-ups',
                           reply_markup=push_ups_kb)


# -------------------------------------------------------------------------------------------------------------------------------
async def bars(message: types.Message):
    if s.query(Users.id).filter(Users.id == message.from_user.id).first() and not s.query(Workout.users_id).filter(Workout.users_id == message.from_user.id).first():
        await message.answer('Write to me how much you did push-ups, I will add it to pushups for the day')
    elif not s.query(Users.id).filter(Users.id == message.from_user.id).first():
        await bot.send_message(message.from_user.id, 'Please register', reply_markup=unregistered_user_kb_reg)
    else:
        await bot.send_message(message.from_user.id, f'Today you did {s.query(Workout).get(message.from_user.id).bars_today} bars', reply_markup=bars_kb)


async def Add_bars(message: types.Message):
    await FSMbars.bars.set()
    await message.answer('Enter the number of bars:')


async def save_bars(message: types.Message,  state: FSMContext):
    s.query(Workout).get(message.from_user.id).bars_today += int(message.text)
    s.query(Workout).get(message.from_user.id).bars_all += int(message.text)
    s.commit()
    s.close()
    await state.finish()
    await bot.send_message(message.from_user.id,
                           f'Today you did {s.query(Workout).get(message.from_user.id).bars_today} bars',
                           reply_markup=bars_kb)
# -----------------------------------------------------------------------------------------------------------------------------


async def pull_ups(message: types.Message):
    if s.query(Users.id).filter(Users.id == message.from_user.id).first() and not s.query(Workout.users_id).filter(Workout.users_id == message.from_user.id).first():
        await message.answer('Write to me how much you did push-ups, I will add it to pullups for the day')
    elif not s.query(Users.id).filter(Users.id == message.from_user.id).first():
        await bot.send_message(message.from_user.id, 'Please register', reply_markup=unregistered_user_kb_reg)
    else:
        await bot.send_message(message.from_user.id, f'Today you did {s.query(Workout).get(message.from_user.id).pull_ups_today} pullups', reply_markup=pull_ups_kb)


async def add_pull_ups(message: types.Message):
    await FSMpull_ups.pull_ups.set()
    await message.answer('Enter the number of pullups:')


async def save_pull_ups(message: types.Message,  state: FSMContext):
    s.query(Workout).get(message.from_user.id).pull_ups_today += int(message.text)
    s.query(Workout).get(message.from_user.id).pull_ups_all += int(message.text)
    s.commit()
    s.close()
    await state.finish()
    await bot.send_message(message.from_user.id,
                           f'Today you did {s.query(Workout).get(message.from_user.id).pull_ups_today} pullups',
                           reply_markup=pull_ups_kb)


# ------------------------------------------------------------------------------------------------------------------------------
async def boys(message: types.Message):
    await SqlLiteDb.sql_read(message)


async def creator(message: types.Message):
    await bot.send_message(message.from_user.id, 'Admin: @sem4ek')
    if message.chat.type != 'private':
        await message.delete()


async def ok():
    for i in s.query(Water).all():
        s.query(Water).get(i.id).glass_of_water_today = 0
    for i in s.query(Workout).all():
        s.query(Workout).get(i.id).push_ups_today = 0
        s.query(Workout).get(i.id).bars_today = 0
        s.query(Workout).get(i.id).pull_ups_today = 0
    s.commit()
    s.close()


async def data_null():
    aioschedule.every(1).day.at('21:00').do(ok)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def all_ex(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'''Push ups: {s.query(Workout).get(message.from_user.id).push_ups_all}
Bars: {s.query(Workout).get(message.from_user.id).bars_all}
Pull ups: {s.query(Workout).get(message.from_user.id).pull_ups_all}''',
                           reply_markup=profile_kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(profile, commands=['Registration'])
    dp.register_message_handler(profile, commands=['profile'], state=None)
    dp.register_message_handler(add_nickname, state=FSMregistr.Nickname)
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(commands_help, commands=['Help'])
    dp.register_message_handler(water, commands=['water'], state=None)
    dp.register_message_handler(status_water, state=FSMwater.start)
    dp.register_message_handler(AddOne, commands=['AddOne'])

    dp.register_message_handler(workout_w, commands=['workout'], state=None)
    dp.register_message_handler(status_workout, state=FSMworkout.start)

    dp.register_message_handler(push_ups, commands=['push_ups'])
    dp.register_message_handler(Add_push_ups, commands=['AddPushUps'], state=None)
    dp.register_message_handler(save_push_ups, state=FSMpush_ups.push_ups)

    dp.register_message_handler(bars, commands=['Bars'])
    dp.register_message_handler(Add_bars, commands=['AddBars'], state=None)
    dp.register_message_handler(save_bars, state=FSMbars.bars)

    dp.register_message_handler(pull_ups, commands=['pull_ups'])
    dp.register_message_handler(add_pull_ups, commands=['AddPullUps'], state=None)
    dp.register_message_handler(save_pull_ups, state=FSMpull_ups.pull_ups)

    dp.register_message_handler(all_ex, commands=['all'])

    dp.register_message_handler(boys, commands=['boys'])
    dp.register_message_handler(creator, commands=['admin'])