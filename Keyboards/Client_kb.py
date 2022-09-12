from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from Handlers import Client

b1 = KeyboardButton('/PROFIL')
b2 = KeyboardButton('/HELP')
# b5 = KeyboardButton('/Registration')
b6 = KeyboardButton('/expenses')
b7 = KeyboardButton('/Sport')
b8 = KeyboardButton('/Add')
b9 = KeyboardButton(f'/Push_ups')
b10 = KeyboardButton('/Bars')
b11 = KeyboardButton('/Pull_ups')
b12 = KeyboardButton('/AddPushUps')
b13 = KeyboardButton('/AddBars')
b14 = KeyboardButton('/AddPullUps')
b15 = KeyboardButton('Русский')
b16 = KeyboardButton('English')
b17 = KeyboardButton('/statistics')
b18 = KeyboardButton('/BYN')
b19 = KeyboardButton('/USD')



main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b1, b2)
unregistered_user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b2)
# unregistered_user_kb_reg = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b5)
profile_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b6, b7)
water_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b8, b1)
workout_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b9, b10, b11).add(b17).add(b1)
push_ups_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b12, b7)
bars_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b13, b7)
pull_ups_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b14, b7)
language_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b16, b15)
valuta_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b18, b19)