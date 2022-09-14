from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


b1 = KeyboardButton('/ПРОФИЛЬ')
b2 = KeyboardButton('/ПОМОЩЬ')
b3 = KeyboardButton('где я', request_location=True)
b6 = KeyboardButton('/РАСХОДЫ')
b7 = KeyboardButton('/СПОРТ')
b9 = KeyboardButton('/ОТЖИМАНИЯ')
b12 = KeyboardButton('/ДОБАВИТЬ_ОТЖИМАНИЯ')
b10 = KeyboardButton('/БРУСЬЯ')
b13 = KeyboardButton('/ДОБАВИТЬ_БРУСЬЯ')
b11 = KeyboardButton('/ПОДТЯГИВАНИЯ')
b14 = KeyboardButton('/ДОБАВИТЬ_ПОДТЯГИВАНИЯ')
b17 = KeyboardButton('/СТАТИСТИКА')
b18 = KeyboardButton('/ДОБАВИТЬ_РАСХОД')
b19 = KeyboardButton('/СТАТИСТИКА_РАСХОДОВ')
b20 = KeyboardButton('ЗА ДЕНЬ')
b21 = KeyboardButton('ЗА МЕСЯЦ')


inline_btn_1 = InlineKeyboardButton('ПЕРЕВЕСТИ В USD', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('ПЕРЕВЕСТИ В BYN', callback_data='button2')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)


main_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b1, b2)
unregistered_user_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b2)
profile_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b6, b7)
workout_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b9, b10, b11).add(b17).add(b1)
push_ups_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b12, b7)
bars_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b13, b7)
pull_ups_kb_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b14, b7)
rof = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b18, b19)
statistics = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(b20, b21)