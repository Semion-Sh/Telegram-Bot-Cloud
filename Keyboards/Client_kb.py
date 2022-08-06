from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton('/Profile')
b2 = KeyboardButton('/Help')
b3 = KeyboardButton('/Bible')
b4 = KeyboardButton('где я', request_location=True)
b5 = KeyboardButton('/Registration')
b6 = KeyboardButton('/Water')
b7 = KeyboardButton('/Workout')
b8 = KeyboardButton('/AddOne')



main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b1, b2)
unregistered_user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b5, b2)
profile_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b6, b7)
water_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b8)