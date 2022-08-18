from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData


Base = declarative_base()
meta = MetaData()


engine = create_engine("postgresql+psycopg2://tcaxbxkflmhevo:90223b7a16f2f49eaf1ac99f16723bd6c12338098988fcc233082e1ed4c58fc7@ec2-54-86-106-48.compute-1.amazonaws.com/dcojkrta6k2u9r")
conn = engine.connect()


session = sessionmaker(bind=engine)