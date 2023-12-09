from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import Session
from models import Base
from sqlalchemy.ext.declarative import declarative_base

class reserva_controller:

    def __init__(self, session: Session):
        self.session = session