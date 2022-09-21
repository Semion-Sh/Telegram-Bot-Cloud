from sqlalchemy import Column, String, Integer, Float, ForeignKey, LargeBinary, VARCHAR, TEXT, DateTime
from DateBase.DATABASE import Base, engine
import datetime
from sqlalchemy.sql import func


class Photo(Base):
    __tablename__ = 'sport_photo'

    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    tg_username = Column(String)
    pic_before = Column(TEXT, default='')
    date_pic_before = Column(DateTime(timezone=True), server_default=func.now())
    pic_after = Column(TEXT, default='')
    date_pic_after = Column(DateTime(timezone=True), onupdate=func.now())


Base.metadata.create_all(engine)
