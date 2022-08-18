from sqlalchemy import Column, Integer, ForeignKey, String
from DateBase.DATABASE import Base, engine


class Workout(Base):
    __tablename__ = 'workout'

    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    tg_name = Column(String)
    push_ups_today = Column(Integer, default=0)
    bars_today = Column(Integer, default=0)
    pull_ups_today = Column(Integer, default=0)
    push_ups_all = Column(Integer, default=0)
    bars_all = Column(Integer, default=0)
    pull_ups_all = Column(Integer, default=0)


Base.metadata.create_all(engine)