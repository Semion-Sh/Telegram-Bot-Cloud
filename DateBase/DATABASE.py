from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from faker import Faker
from sqlalchemy import Column, String, Integer
import os

Base = declarative_base()
meta = MetaData()
DATABASE_NAME = 'profiles.db'


engine = create_engine(f'sqlite:///{DATABASE_NAME}')
conn = engine.connect()
db_is_created = os.path.exists(DATABASE_NAME)


def create_db():
    if not db_is_created:
        print(f'Data base {DATABASE_NAME} created successfully!')
        meta.create_all(engine)


session = sessionmaker(bind=engine)


def _load_fake_data(session: session):
    ...


def create_database(load_fake_data: bool=True):
    create_db()
    if load_fake_data:
        _load_fake_data(session())
