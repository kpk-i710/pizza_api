from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy_utils.types import ChoiceType

engine = create_engine('psostgresql://postgres:nathanoj35@localhost/pizza_deliv', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    password = Column(Text, unique=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User {self.username}"


class Choise(Base):
    ORDER_STATUSES = (('PENDING', 'pending',),
                      ('IN-TRANSIT','in-trainsit'),
                      ('DELIVERED','delivered')
                      )

    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
