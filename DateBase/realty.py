from sqlalchemy import Column, String, Integer, Date
from DateBase.DATABASE import Base, engine


class NorthCyprusRealty(Base):
    __tablename__ = 'NorthCyprusRealty'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)
    square = Column(Integer)
    city_complex = Column(String)
    floor = Column(String)
    floor_count = Column(String)
    type = Column(String)
    rooms = Column(String)
    data_add = Column(Date)
    data_update = Column(Date)
    old = Column(Integer)

Base.metadata.create_all(engine)