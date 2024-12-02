from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils import ChoiceType

from database  import engine, Base
from database import engine


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение к базе данных
DATABASE_URL = "mysql+mysqlconnector://p585477_rafael:560200Gram@185.105.110.6/p585477_rafael"
engine = create_engine(DATABASE_URL, echo=True)
from models import  User, Order
# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Создание сессии для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()


# Пример добавления данных в таблицы
new_user = User(username='john_doe', email='john@example.com', password='securepassword', is_staff=True, is_active=True)
new_order = Order(quantity=2, order_status='PENDING', pizza_size='LARGE', user=new_user)

session.add(new_user)
session.add(new_order)
session.commit()

# Закрытие сессии
session.close()