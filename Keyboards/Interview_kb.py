from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# b1 = KeyboardButton('/собеседование')
b2 = KeyboardButton('/конец')


interview_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b2)
