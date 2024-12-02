
from database  import engine, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum as EnumType
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    password = Column(String(255), unique=True)  # Изменено на String с ограничением длины
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f"<User {self.username}>"

class Order(Base):
    ORDER_STATUSES = (
        'PENDING',
        'IN-TRANSIT',
        'DELIVERED'
    )

    PIZZA_SIZES = (
        'SMALL',
        'MEDIUM',
        'LARGE',
        'EXTRA-LARGE'
    )

    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(EnumType(*ORDER_STATUSES, name='order_status_enum'), default="PENDING")
    pizza_size = Column(EnumType(*PIZZA_SIZES, name='pizza_size_enum'), default='SMALL')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='orders')

    def __repr__(self):
        return f"<Order {self.id}>"