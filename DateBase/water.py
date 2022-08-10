from sqlalchemy import Column, Integer, ForeignKey, String
from DateBase.DATABASE import Base, engine
from sqlalchemy.orm import relationship


class Water(Base):
    __tablename__ = 'water'

    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    tg_name = Column(String)
    glass_of_water_today = Column(Integer, default=0)


Base.metadata.create_all(engine)