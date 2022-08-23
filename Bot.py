from create_bot import dp, bot
from aiogram.utils import executor
from Handlers import Client, Other, Admin
import asyncio
from Handlers.Other import spam_start
from Handlers.Other import bot_commands
from DateBase import DATABASE
import os
from Handlers.Client import data_null


async def start_bot(_):
    asyncio.create_task(spam_start())
    asyncio.create_task(data_null())
    await bot.set_my_commands(bot_commands)


Client.register_handlers_client(dp)
Other.register_handlers_other(dp)
# Admin.register_handlers_admin(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)