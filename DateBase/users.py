from sqlalchemy import Column, String, Integer
from DateBase.DATABASE import Base, engine


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nick = Column(String)
    tg_username = Column(String)


Base.metadata.create_all(engine)


# def sql_start():
#     global base, cur
#     base = sq.connect('users_profile.db')
#     cur = base.cursor()
#     if base:
#         print('Data base db_profile connected successfully!')
#     # base.execute('CREATE TABLE IF NOT EXISTS users(id integer primary key AUTOINCREMENT, nickname varchar(60))')
#     base.execute('CREATE TABLE IF NOT EXISTS users(user_id integer primary key, nickname TEXT, tg_user_name TEXT)')
#     base.commit()
#
#
# async def sql_add_command(state):
#     async with state.proxy() as data:
#         cur.execute('insert into users values(?,?,?)', tuple(data.values()))
#         base.commit()

# async def sql_read(message):
#     for ret in cur.execute('SELECT * FROM users').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nAbout him:{ret[2]}\nGirlfriend: {ret[-1]}')
#
# async def sql_read2():
#     return cur.execute('SELECT * FROM users').fetchall()
#
# async def sql_delete_command(data):
#     cur.execute('DELETE FROM users WHERE nickname == ?', (data,))
#     base.commit()
#
# async def sql_read(message):
#     for ret in cur.execute('SELECT * FROM users').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nAbout him:{ret[2]}\nGirlfriend: {ret[-1]}')