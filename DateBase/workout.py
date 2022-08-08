from sqlalchemy import Column, Integer, ForeignKey
from DateBase.DATABASE import Base, engine
from sqlalchemy.orm import relationship


class Workout(Base):
    __tablename__ = 'workout'

    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    push_ups_today = Column(Integer, default=0)
    bars_today = Column(Integer, default=0)
    pull_ups_today = Column(Integer, default=0)


Base.metadata.create_all(engine)