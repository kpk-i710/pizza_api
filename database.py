from email.policy import default
from random import choice

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship

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
    orders = relationship('Order',back_populates='user')

    def __repr__(self):
        return f"<User {self.username}"




class Order(Base):
    ORDER_STATUSES = (('PENDING', 'pending',),
                      ('IN-TRANSIT', 'in-trainsit'),
                      ('DELIVERED', 'delivered')
                      )

    PIZZA_SIZES = (
        ('SMALL', ' small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA-LARGE', 'extra-large'))

    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES,default = 'SMALL'))
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship('User',back_populates='urders')

    def __repr__(self):
        return f"<Order {self.id}"