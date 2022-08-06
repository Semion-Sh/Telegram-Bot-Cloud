from create_bot import bot


async def football_poll_rafieva_ratomka():
    await bot.send_poll(chat_id='-1001312541304', question='Футбол сегодня:',
                        options=['Рафиева 55, 21:30(начало)', 'Ратомка 21:00(начало)', 'Не буду'],
                        is_anonymous=False)


async def test_football_poll():
    await bot.send_poll(chat_id='-618708229', question='Футбол сегодня:',
                        options=['Рафиева 55, 21:30(начало)', 'Ратомка 21:00(начало)', 'Не буду'],
                        is_anonymous=False)


# -1001312541304 football chat id


# -1001323540103 sky_time