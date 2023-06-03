from sqlalchemy import Column, Integer, String

from database import Base


class Message(Base):
    __tablename__ = 'message'

    id: int = Column('id', Integer, primary_key=True)
    user_id: int = Column('user_id', Integer)
    message: str = Column('message', String, nullable=True)
