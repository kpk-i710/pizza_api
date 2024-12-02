from database  import engine, Base
from models import User, Order
from database import engine

Base.metadata.create_all(bind=engine)