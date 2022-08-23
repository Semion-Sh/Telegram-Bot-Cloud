from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


b1 = KeyboardButton('/Профиль')
b2 = KeyboardButton('/Помощь')
b3 = KeyboardButton('где я', request_location=True)
b5 = KeyboardButton('/Регистрация')
b6 = KeyboardButton('/Вода')
b7 = KeyboardButton('/Воркаут')
b8 = KeyboardButton('/Добавить')
b9 = KeyboardButton('/Отжимания')
b10 = KeyboardButton('/Брусья')
b11 = KeyboardButton('/Подтягивания')
b12 = KeyboardButton('/ДобавитьОтжимания')
b13 = KeyboardButton('/ДобавитьБрусья')
b14 = KeyboardButton('/ДобавитьПодтягивания')


main_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b1, b2)
unregistered_user_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b5, b2)
unregistered_user_kb_reg_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b5)
profile_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b6, b7)
water_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b8, b1)
workout_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b9, b10, b11).add(b1)
push_ups_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b12, b7)
bars_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b13, b7)
pull_ups_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b14, b7)
