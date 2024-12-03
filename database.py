from email.policy import default
from random import choice

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+mysqlconnector://p585477_rafael:560200Gram@185.105.110.6/p585477_rafael"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

# Создание сессии для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()
