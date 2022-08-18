from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData


Base = declarative_base()
meta = MetaData()


engine = create_engine("postgresql+psycopg2://gvaoqrlriwfoad:055f19b677f01b0411151ab91809d03ff4007515e82a428cb9f4148d8badfa54@ec2-52-207-15-147.compute-1.amazonaws.com/dcl69hnioedc5p")
conn = engine.connect()


session = sessionmaker(bind=engine)