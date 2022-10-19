# from sqlalchemy import Column, String, Integer, Float, ForeignKey
# from DateBase.DATABASE import Base, engine
#
#
# class Expenses(Base):
#     __tablename__ = 'expenses'
#
#     id = Column(Integer, primary_key=True)
#     users_id = Column(Integer, ForeignKey('users.id'))
#     tg_username = Column(String)
#     expenses_today = Column(Float, default=0)
#     expenses_mounth = Column(Float, default=0)
#     expenses_all = Column(Float, default=0)
#
#
# Base.metadata.create_all(engine)