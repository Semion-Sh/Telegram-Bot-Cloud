from sqlalchemy import Column, String, Integer
from DateBase.DATABASE import Base, engine


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_username = Column(String)
    language = Column(String)


Base.metadata.create_all(engine)