from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from create_bot import bot, dp
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from DateBase import SqlLiteDb, users
from Keyboards import Admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter


ID = None
Name = None


class FSMAdmin(StatesGroup):
    Photo = State()
    Name = State()
    Description = State()
    Girlfriend = State()


async def make_changes_commands(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'I am listening', reply_markup=Admin_kb.button_case_admin)
    await message.delete()


# start downloading
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.Photo.set()
        await message.answer('Download photo')


# The first answer
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.answer('Name')


# The second answer
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            global Name
            Name = message.text
            data['name'] = message.text
        await FSMAdmin.next()
        await message.answer('Write about him')


# The third answer
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['Description'] = message.text
        await FSMAdmin.next()
        await message.answer(f'Does {Name} have a girlfriend?')


# The fourth answer
async def load_girlfriend(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['Girlfriend'] = message.text

        await SqlLiteDb.sql_add_command(state)
        await state.finish()


# Finish state
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.answer('OK')


async def del_callback_run(callback_query: types.CallbackQuery):
    await SqlLiteDb.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} deleted', show_alert=True)


async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await SqlLiteDb.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nAbout him:{ret[2]}\nGirlfriend: {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'delete {ret[1]}', callback_data=f'del {ret[1]}')))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['upload'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.Photo)
    dp.register_message_handler(load_name, state=FSMAdmin.Name)
    dp.register_message_handler(load_description, state=FSMAdmin.Description)
    dp.register_message_handler(load_girlfriend, state=FSMAdmin.Girlfriend)
    dp.register_message_handler(cancel_handler, state="*", commands='end')
    dp.register_message_handler(cancel_handler, Text(equals='end', ignore_case=True), state='*')
    dp.register_message_handler(make_changes_commands, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(delete_item, commands=['delete'])
    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
