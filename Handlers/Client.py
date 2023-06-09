import asyncio, aioschedule
from Keyboards import rof, photo_ru, inline_kb1, inline_kb2, main_kb, valuta_kb, unregistered_user_kb, profile_kb, \
    workout_kb, push_ups_kb, bars_kb, pull_ups_kb, language_kb, \
    unregistered_user_kb_ru, profile_kb_ru, statistics, workout_kb_ru, push_ups_kb_ru, bars_kb_ru, pull_ups_kb_ru
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot, dp
# from DateBase.users import Users
# from DateBase.workout import Workout
# from DateBase.expenses import Expenses
# from DateBase.sport_photo import Photo
# from DateBase.DATABASE import session
from aiogram import types
from aiogram.dispatcher import Dispatcher
# import psycopg2
# from sqlalchemy import create_engine, update
from aiogram.dispatcher.filters import CommandStart
# from myfin import prodaja, nbrb, pokupka
# from aiogram.types import ContentType
# from sqlalchemy.orm import Session
# from sqlalchemy.orm import sessionmaker
# import requests
# import time
# from urllib.parse import urlencode
# import hmac
# import hashlib
# import time
# from selenium.webdriver.chrome.options import Options
# import Config
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# import os


# conn = psycopg2.connect(host="ec2-52-207-15-147.compute-1.amazonaws.com",
#                         port=5432, database="dcl69hnioedc5p",
#                         user="gvaoqrlriwfoad",
#                         password="055f19b677f01b0411151ab91809d03ff4007515e82a428cb9f4148d8badfa54")
# cur = conn.cursor()
# print("Database opened successfully")

# engine = create_engine("postgresql+psycopg2://gvaoqrlriwfoad:055f19b677f01b0411151ab91809d03ff4007515e82a428cb9f4148d8badfa54@ec2-52-207-15-147.compute-1.amazonaws.com/dcl69hnioedc5p")
# engine.connect()
# s = session()


# def toFixed(numObj, digits=2):
#     return f"{numObj:.{digits}f}"


class FSMregistr(StatesGroup):
    language_ = State()


class FSMpush_ups(StatesGroup):
    push_ups = State()


class FSMbars(StatesGroup):
    bars = State()


class FSMpull_ups(StatesGroup):
    pull_ups = State()


language = ''


#
# async def get_info():
#     values = dict()
#     values["method"] = "getInfo"
#     values["nonce"] = str(int(time.time()))
#
#     body = urlencode(values).encode("utf-8")
#     sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()
#
#     headers = {
#         "key": '5662739762:AAF5slyKUMO0NXcIRMQy1R3ByHkfrBy5ZsQ',
#         "sign": sign
#     }
#
#     response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
#     return response.json()
#
#
# async def get_deposit_address(coin_name="btc"):
#     values = dict()
#     values["method"] = "GetDepositAddress"
#     values["coinName"] = coin_name
#     values["need_new"] = 0
#     values["nonce"] = str(int(time.time()))
#
#     body = urlencode(values).encode("utf-8")
#     sign = hmac.new(API_SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()
#
#     headers = {
#         "key": API_KEY,
#         "sign": sign
#     }
#
#     response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
#     return response.json()
#
#
# async def main():
#     coin_name = input("Enter a coin name: ")
#     print(get_deposit_address(coin_name=coin_name))
#     # print(get_info())


async def commands_start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, f'''Приветствуем, {message.from_user.first_name}, Cyprus Realty bot
Это бот для поиска и продажи недвижимости на Кипре

Здесь вы можете создать свой запрос и начать получать предложения от живых риелторов.
Если предложение не подходит, то вы можете отклонить его и продолжить получать другие варианты. Если вы получите подходящее предложение, то можете принять его и продолжить общение с риелтором.

- Это абсолютно бесплатно
- Обширная база недвижимости
- Конфиденциальность. Только вы решаете кому давать свой номер телефона

Вы можете создать заявку, нажав на кнопку «Создать заявку»''')


#
# async def choose_language(message: types.Message, state: FSMContext):
#     id = message.from_user.id
#     global language
#     if message.text in ['Russian', 'Русский', 'РУССКИЙ']:
#         language = 'Russian'
#         await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}',
#                                 reply_markup=unregistered_user_kb_ru)
#     elif message.text in ['English', 'Английский', 'ENGLISH']:
#         language = 'English'
#         await bot.send_message(message.from_user.id, f'Hello, {message.from_user.first_name}',
#                                 reply_markup=unregistered_user_kb)
#     if message.from_user.username != None:
#         tg_username = '@' + message.from_user.username
#     else: tg_username = 'Not'
#     if language == 'English':
#         user = Users(id=id, tg_username=tg_username, language='English')
#     elif language == 'Russian':
#         user = Users(id=id, tg_username=tg_username, language='Russian')
#     await state.finish()
#     s.add(user)
#     s.commit()
#     s.close()
#
#
# async def profile(message: types.Message):
#     if s.query(Users.id).filter(Users.id == message.from_user.id).first() and \
#             s.query(Users).get(message.from_user.id).language == 'English':
#         await bot.send_message(message.from_user.id, '-', reply_markup=profile_kb)
#     elif s.query(Users.id).filter(Users.id == message.from_user.id).first() and \
#             s.query(Users).get(message.from_user.id).language == 'Russian':
#         await bot.send_message(message.from_user.id, '-', reply_markup=profile_kb_ru)
#
#
# async def commands_help(message: types.Message):
#     if s.query(Users).get(message.from_user.id).language == 'Russian':
#         await bot.send_message(message.from_user.id, '''
#         Список команд:
# /PROFILE - ваш профиль
# /ADMIN - создатель Бота
# /SPORT - спортивная активность
# /STATISTICS - статистика за весь период
# /EXPENSES - учет расходов
# ''')
#     elif s.query(Users).get(message.from_user.id).language == 'English':
#         await bot.send_message(message.from_user.id, '''
#         Command List:
# /PROFILE - your profile
# /ADMIN - Bot creator
# /SPORT - sports activity
# /STATISTICS - statistics for the entire period
# /EXPENSES - cost accounting
# ''')
#
#
# async def photo_menu(message: types.Message):
#     await bot.send_message(message.from_user.id, '-', reply_markup=photo_ru)
#
#
# async def workout_photo(message: types.Message):
#     if message.from_user.username != None:
#         tg_username = '@' + message.from_user.username
#     else:
#         tg_username = 'Not'
#     if s.query(Photo.id).filter(Photo.id == message.from_user.id).first():
#         if s.query(Photo).get(message.from_user.id).pic_before != '':
#             await bot.send_message(message.from_user.id, 'send me photo of your progres body')
#         else:
#             await bot.send_message(message.from_user.id, 'send me the first photo of your body')
#     else:
#         photo = Photo(id=message.from_user.id, tg_username=tg_username, users_id=message.from_user.id)
#         s.add(photo)
#         s.commit()
#         s.close()
#
#
# async def workout_save(message: types.Message):
#     if message.from_user.username != None:
#         tg_username = '@' + message.from_user.username
#     else:
#         tg_username = 'Not'
#     document_id = message.photo[-1].file_id
#     file_info = await bot.get_file(document_id)
#     if s.query(Photo).get(message.from_user.id).pic_before != '':
#         s.query(Photo).get(message.from_user.id).pic_after = file_info.file_id
#     else:
#         s.query(Photo).get(message.from_user.id).pic_before = file_info.file_id
#     s.commit()
#     s.close()
#
#
# async def send_foto(message: types.Message):
#     date_before = {
#         'year': str(s.query(Photo).get(message.from_user.id).date_pic_before)[:4],
#         'mounth': str(s.query(Photo).get(message.from_user.id).date_pic_before)[4:8],
#         'day': str(s.query(Photo).get(message.from_user.id).date_pic_before)[8:10]
#     }
#
#     date_after = {
#         'year': str(s.query(Photo).get(message.from_user.id).date_pic_after)[:4],
#         'mounth': str(s.query(Photo).get(message.from_user.id).date_pic_after)[4:8],
#         'day': str(s.query(Photo).get(message.from_user.id).date_pic_after)[8:10]
#     }
#     await bot.send_message(message.from_user.id, date_before['day']+date_before['mounth']+date_before['year'])
#     await bot.send_photo(message.from_user.id, photo=s.query(Photo).get(message.from_user.id).pic_before)
#
#     await bot.send_message(message.from_user.id, date_after['day']+date_after['mounth']+date_after['year'])
#     await bot.send_photo(message.from_user.id,
#                          photo=s.query(Photo).get(message.from_user.id).pic_after,
#                          reply_markup=profile_kb_ru)
#
#
#
# async def workout_w(message: types.Message):
#     if not s.query(Workout.id).filter(Workout.id == message.from_user.id).first():
#         workout = Workout(id=message.from_user.id,
#                           users_id=message.from_user.id,
#                           tg_name='@' + message.from_user.username)
#         s.add(workout)
#         s.commit()
#         s.close()
#         if s.query(Users).get(message.from_user.id).language == 'English':
#             await bot.send_message(message.from_user.id, '-', reply_markup=workout_kb)
#         else:
#             await bot.send_message(message.from_user.id, '-', reply_markup=workout_kb_ru)
#     else:
#         if s.query(Users).get(message.from_user.id).language == 'English':
#             await bot.send_message(message.from_user.id, '-', reply_markup=workout_kb)
#         else:
#             await bot.send_message(message.from_user.id, '-', reply_markup=workout_kb_ru)
#
#
# count = 0
#
#
# async def push_ups(message: types.Message):
#     global count
#     count = s.query(Workout).get(message.from_user.id).pull_ups_today
#     if s.query(Users.id).filter(Users.id == message.from_user.id).first() and \
#             not s.query(Workout.users_id).filter(Workout.users_id == message.from_user.id).first():
#         await message.answer('Write to me how much you did push-ups, I will add it to pushups for the day')
#     else:
#         if s.query(Users).get(message.from_user.id).language == 'English':
#             await bot.send_message(message.from_user.id,
#                                    f'Today you did {s.query(Workout).get(message.from_user.id).push_ups_today} push-ups',
#                                    reply_markup=push_ups_kb)
#         else:
#             await bot.send_message(message.from_user.id,
#                                    f'Сегодня ты сделал {s.query(Workout).get(message.from_user.id).push_ups_today} отжиманий',
#                                    reply_markup=push_ups_kb_ru)
#
#
# async def Add_push_ups(message: types.Message):
#     await FSMpush_ups.push_ups.set()
#     if s.query(Users).get(message.from_user.id).language == 'English':
#         await message.answer('Enter the number of pushups:')
#     else:
#         await message.answer('Введите количество отжиманий:')
#
#
# async def save_push_ups(message: types.Message,  state: FSMContext):
#     try:
#         s.query(Workout).get(message.from_user.id).push_ups_today += int(message.text)
#         s.query(Workout).get(message.from_user.id).push_ups_all += int(message.text)
#         s.commit()
#         s.close()
#         if s.query(Users).get(message.from_user.id).language == 'English':
#             await bot.send_message(message.from_user.id,
#                                f'Today you did {s.query(Workout).get(message.from_user.id).push_ups_today} push-ups',
#                                reply_markup=push_ups_kb)
#         else:
#             await bot.send_message(message.from_user.id,
#                                    f'Сегодня ты сделал {s.query(Workout).get(message.from_user.id).push_ups_today} отжиманий',
#                                    reply_markup=push_ups_kb_ru)
#     except:
#         if s.query(Users).get(message.from_user.id).language == 'English':
#             await bot.send_message(message.from_user.id,
#                                f'Pushups have not been added',
#                                reply_markup=push_ups_kb)
#         else:
#             await bot.send_message(message.from_user.id,
#                                    f'Отжимания не были добавлены',
#                                    reply_markup=push_ups_kb_ru)
#     await state.finish()
#
#
# async def bars(message: types.Message):
#     if s.query(Users.id).filter(Users.id == message.from_user.id).first() and \
#             not s.query(Workout.users_id).filter(Workout.users_id == message.from_user.id).first():
#         await message.answer('Write to me how much you did push-ups, I will add it to pushups for the day')
#     else:
#         if s.query(Users).get(message.from_user.id).language == 'English':
#             await bot.send_message(message.from_user.id,
#                                    f'Today you did {s.query(Workout).get(message.from_user.id).bars_today} bars',
#                                    reply_markup=bars_kb)
#         else:
#             await bot.send_message(message.from_user.id,
#                                    f'Сегодня ты сделал {s.query(Workout).get(message.from_user.id).bars_today} отжиманий на брусьях',
#                                    reply_markup=bars_kb_ru)
#
#
# async def Add_bars(message: types.Message):
#     await FSMbars.bars.set()
#     if s.query(Users).get(message.from_user.id).language == 'English':
#         await message.answer('Enter the number of bars:')
#     else:
#         await message.answer('Введите количество отжиманий на брусьях:')
#
#
# async def save_bars(message: types.Message,  state: FSMContext):
#     try:
#         s.query(Workout).get(message.from_user.id).bars_today += int(message.text)
#         s.query(Workout).get(message.from_user.id).bars_all += int(message.text)
#         s.commit()
#         s.close()
#         if s.query(Users).get(message.from_user.id).language == 'English':
#             await bot.send_message(message.from_user.id,
#                                f'Today you did {s.query(Workout).get(message.from_user.id).bars_today} bars',
#                                reply_markup=bars_kb)
#         else:
#             await bot.send_message(message.from_user.id,
#                            f'Сегодня ты сделал {s.query(Workout).get(message.from_user.id).bars_today} отжиманий на брусьях',
#                            reply_markup=bars_kb_ru)
#     except:
#         if s.query(Users).get(message.from_user.id).language == 'English':
#             await bot.send_message(message.from_user.id,
#                                f'Bars have not been added',
#                                reply_markup=bars_kb)
#         else:
#             await bot.send_message(message.from_user.id,
#                                    f'Отжимания не были добавлены',
#                                    reply_markup=bars_kb_ru)
#     await state.finish()
#
#
# async def pull_ups(message: types.Message):
#     if s.query(Users.id).filter(Users.id == message.from_user.id).first() and \
#             not s.query(Workout.users_id).filter(Workout.users_id == message.from_user.id).first():
#         await message.answer('Write to me how much you did push-ups, I will add it to pullups for the day')
#     else:
#         if s.query(Users).get(message.from_user.id).language == 'English':
#             await bot.send_message(message.from_user.id,
#                                    f'Today you did {s.query(Workout).get(message.from_user.id).pull_ups_today} pullups',
#                                    reply_markup=pull_ups_kb)
#         else:
#             await bot.send_message(message.from_user.id, f'Сегодня ты сделал {s.query(Workout).get(message.from_user.id).pull_ups_today} подтягиваний', reply_markup=pull_ups_kb_ru)
#
#
# async def add_pull_ups(message: types.Message):
#     await FSMpull_ups.pull_ups.set()
#     if s.query(Users).get(message.from_user.id).language == 'English':
#         await message.answer('Enter the number of pullups:')
#     else:
#         await message.answer('Введите количество подтягиваний:')
#
#
# async def save_pull_ups(message: types.Message,  state: FSMContext):
#     try:
#         s.query(Workout).get(message.from_user.id).pull_ups_today += int(message.text)
#         s.query(Workout).get(message.from_user.id).pull_ups_all += int(message.text)
#         s.commit()
#         s.close()
#         if s.query(Users).get(message.from_user.id).language == 'English':
#             await bot.send_message(message.from_user.id,
#                                f'Today you did {s.query(Workout).get(message.from_user.id).pull_ups_today} pullups',
#                                reply_markup=pull_ups_kb)
#         else:
#             await bot.send_message(message.from_user.id,
#                                    f'Сегодня ты сделал {s.query(Workout).get(message.from_user.id).pull_ups_today} подтягиваний',
#                                    reply_markup=pull_ups_kb_ru)
#
#     except:
#         if s.query(Users).get(message.from_user.id).language == 'English':
#             await bot.send_message(message.from_user.id,
#                                f'Pullups have not been added',
#                                reply_markup=pull_ups_kb)
#         else:
#             await bot.send_message(message.from_user.id,
#                                f'Подтягивания не были добавлены',
#                                reply_markup=pull_ups_kb_ru)
#     await state.finish()
#
#
#
#
# async def remove_today_data():
#     for i in s.query(Workout).all():
#         s.query(Workout).get(i.id).push_ups_today = 0
#         s.query(Workout).get(i.id).bars_today = 0
#         s.query(Workout).get(i.id).pull_ups_today = 0
#     s.commit()
#     s.close()
#
#
# async def data_null():
#     aioschedule.every(1).day.at('21:00').do(remove_today_data)
#     aioschedule.every(1).day.at('21:00').do(remove_today_finance_data)
#     aioschedule.every(1).monday.at('21:00').do(remove_today_finance_data)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)
#
#
# async def all_ex(message: types.Message):
#     if s.query(Users).get(message.from_user.id).language == 'English':
#         await bot.send_message(message.from_user.id, f'''
#                            All the time you did
# Push ups: {s.query(Workout).get(message.from_user.id).push_ups_all}
# Bars: {s.query(Workout).get(message.from_user.id).bars_all}
# Pull ups: {s.query(Workout).get(message.from_user.id).pull_ups_all}''',
#                            reply_markup=profile_kb)
#     else:
#         await bot.send_message(message.from_user.id, f'''
#                                    За всё время ты сделал
# Отжимания: {s.query(Workout).get(message.from_user.id).push_ups_all}
# Брусья: {s.query(Workout).get(message.from_user.id).bars_all}
# Подтягивания: {s.query(Workout).get(message.from_user.id).pull_ups_all}''',
#                                reply_markup=profile_kb_ru)
#
#
# class FSMmoney(StatesGroup):
#     valuta_ = State()
#     money = State()
#
#
# async def expenses_def(message: types.Message):
#     if not s.query(Expenses.id).filter(Expenses.id == message.from_user.id).first():
#         if message.from_user.username != None:
#             tg_username = '@' + message.from_user.username
#         else:
#             tg_username = 'Not'
#         expenses = Expenses(id=message.from_user.id, tg_username=tg_username, users_id=message.from_user.id)
#         s.add(expenses)
#         s.commit()
#         s.close()
#     await FSMmoney.valuta_.set()
#     await bot.send_message(message.from_user.id, f'ВЫБЕРИТЕ ВАЛЮТУ:', reply_markup=valuta_kb)
#
# valuta_var = None
#
#
# async def valuta(message: types.Message, state: FSMContext):
#     global valuta_var
#     if message.text == '/BYN':
#         valuta_var = 'BYN'
#         await bot.send_message(message.from_user.id, f'ВВЕДИТЕ СУММУ В BYN:')
#     elif message.text == '/USD':
#         valuta_var = 'USD'
#         await bot.send_message(message.from_user.id, f'ВВЕДИТЕ СУММУ В USD:')
#     else:
#         await bot.send_message(message.from_user.id, f'-', reply_markup=profile_kb_ru)
#         await state.finish()
#     await FSMmoney.money.set()
#
#
# async def expenses(message: types.Message):
#     await bot.send_message(message.from_user.id,
#                            f'-',
#                            reply_markup=rof)
#
#
# async def expenses_save(message: types.Message, state: FSMContext):
#     global valuta_var
#     # await state.update_data(money=message.text)
#     # data = await state.get_data()
#     # count = data.get('money')
#     try:
#         if valuta_var == 'BYN':
#             s.query(Expenses).get(message.from_user.id).expenses_today += float(message.text)
#             s.query(Expenses).get(message.from_user.id).expenses_mounth += float(message.text)
#             s.query(Expenses).get(message.from_user.id).expenses_all += float(message.text)
#             await bot.send_message(message.from_user.id,
#                                    f'СЕГОДНЯ ТЫ ПОТРАТИЛ(А) - {toFixed(s.query(Expenses).get(message.from_user.id).expenses_today)} BYN',
#                                    reply_markup=inline_kb1)
#         elif valuta_var == 'USD':
#             x = float(message.text) * nbrb
#             s.query(Expenses).get(message.from_user.id).expenses_today += x
#             s.query(Expenses).get(message.from_user.id).expenses_mounth += x
#             s.query(Expenses).get(message.from_user.id).expenses_all += x
#             await bot.send_message(message.from_user.id,
#                                    f'СЕГОДНЯ ТЫ ПОТРАТИЛ(А) - {toFixed(s.query(Expenses).get(message.from_user.id).expenses_today // nbrb)}$',
#                                    reply_markup=inline_kb2)
#     except:
#         await bot.send_message(message.from_user.id,
#                                f'НЕ ДОБАВЛЕНО',
#                                reply_markup=profile_kb)
#     await state.finish()
#     s.commit()
#     s.close()
#
#
# class FSMstatistics_kind(StatesGroup):
#     kind = State()
#
#
# async def statistics_expenses(message: types.Message):
#     await bot.send_message(message.from_user.id,
#                            f'-', reply_markup=statistics)
#     await FSMstatistics_kind.kind.set()
#
#
# async def statistics_expenses_kind(message: types.Message, state: FSMContext):
#     if message.text == 'ЗА ДЕНЬ':
#         await bot.send_message(message.from_user.id,
#                                f'СЕГОДНЯ ТЫ ПОТРАТИЛ(А) - {toFixed(s.query(Expenses).get(message.from_user.id).expenses_today)}BYN',
#                                reply_markup=inline_kb1)
#     if message.text == 'ЗА МЕСЯЦ':
#         await bot.send_message(message.from_user.id,
#                                f'ЗА ЭТОТ МЕСЯЦ ТЫ ПОТРАТИЛ(А) - {toFixed(s.query(Expenses).get(message.from_user.id).expenses_mounth)}BYN',
#                                reply_markup=inline_kb1)
#     await state.finish()
#
#
# @dp.callback_query_handler(text='button1')
# async def process_callback_button1(message: types.Message):
#     await bot.send_message(message.from_user.id,
#                            f'СЕГОДНЯ ТЫ ПОТРАТИЛ(А) - {toFixed(s.query(Expenses).get(message.from_user.id).expenses_today//prodaja)}$',
#                            reply_markup=profile_kb_ru)
#
#
# @dp.callback_query_handler(text='button2')
# async def process_callback_button1(message: types.Message):
#     await bot.send_message(message.from_user.id,
#                            f'СЕГОДНЯ ТЫ ПОТРАТИЛ(А) - {toFixed(s.query(Expenses).get(message.from_user.id).expenses_today)} BYN',
#                            reply_markup=profile_kb_ru)
#
#
# async def remove_today_finance_data():
#     for i in s.query(Expenses).all():
#         s.query(Expenses).get(i.id).expenses_today = 0
#     s.commit()
#     s.close()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, CommandStart(), state=None)
    # dp.register_message_handler(english, commands=['english'])
    # dp.register_message_handler(main, commands=['crypto'])
#     dp.register_message_handler(choose_language, state=FSMregistr.language_)
#     dp.register_message_handler(profile, commands=['profile', 'ПРОФИЛЬ'])
#     dp.register_message_handler(commands_help, commands=['HELP', 'ПОМОЩЬ'])
#
#     dp.register_message_handler(photo_menu, commands=['PHOTO', 'ФОТО'])
#     dp.register_message_handler(workout_photo, commands=['DOWNLOAD', 'ЗАГРУЗИТЬ'])
#     dp.register_message_handler(workout_save, content_types=ContentType.PHOTO)
#     dp.register_message_handler(send_foto, commands=['SEE', 'ПОСМОТРЕТЬ'])
#
#
#     dp.register_message_handler(workout_w, commands=['SPORT', 'СПОРТ'])
#
#     dp.register_message_handler(push_ups, commands=[f'PUSH_UPS', 'ОТЖИМАНИЯ'])
#     dp.register_message_handler(Add_push_ups, commands=['ADD_PUSH_UPS', 'ДОБАВИТЬ_ОТЖИМАНИЯ'], state=None)
#     dp.register_message_handler(save_push_ups, state=FSMpush_ups.push_ups)
#
#     dp.register_message_handler(bars, commands=['BARS', 'БРУСЬЯ'])
#     dp.register_message_handler(Add_bars, commands=['ADD_BARS', 'ДОБАВИТЬ_БРУСЬЯ'], state=None)
#     dp.register_message_handler(save_bars, state=FSMbars.bars)
#
#     dp.register_message_handler(pull_ups, commands=['PULL_UPS', 'ПОДТЯГИВАНИЯ'])
#     dp.register_message_handler(add_pull_ups, commands=['ADD_PULL_UPS', 'ДОБАВИТЬ_ПОДТЯГИВАНИЯ'], state=None)
#     dp.register_message_handler(save_pull_ups, state=FSMpull_ups.pull_ups)
#
#     dp.register_message_handler(all_ex, commands=['STATISTICS', 'СТАТИСТИКА'])

#
#
#     dp.register_message_handler(expenses, commands=['EXPENSES', 'РАСХОДЫ'],)
#
#     dp.register_message_handler(statistics_expenses, commands=['STATISTICS_EXPENSES', 'СТАТИСТИКА_РАСХОДОВ'], state=None)
#     dp.register_message_handler(statistics_expenses_kind, state=FSMstatistics_kind.kind)
#     dp.register_message_handler(expenses_def, commands=['ADD_EXPENSE', 'ДОБАВИТЬ_РАСХОД'], state=None)
#     dp.register_message_handler(valuta, state=FSMmoney.valuta_)
#     dp.register_message_handler(expenses_save, state=FSMmoney.money)
#
