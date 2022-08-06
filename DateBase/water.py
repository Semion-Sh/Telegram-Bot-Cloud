from sqlalchemy import Column, Integer, ForeignKey, BOOLEAN
from DateBase.DATABASE import Base, engine
from sqlalchemy.orm import relationship


class Water(Base):
    __tablename__ = 'water'

    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    glass_of_water_today = Column(Integer, default=0)
    # status = Column(BOOLEAN, default=False)


Base.metadata.create_all(engine)