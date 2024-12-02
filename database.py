from email.policy import default
from random import choice

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base




engine = create_engine('psostgresql://postgres:nathanoj35@localhost/pizza_deliv', echo=True)

Base = declarative_base()
