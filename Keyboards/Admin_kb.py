from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_load = KeyboardButton('/Upload')
button_delete = KeyboardButton('️/Delete')
button_end = KeyboardButton('️/end')


button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_load, button_delete)
button_fsm_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_end)
