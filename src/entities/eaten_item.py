from sqlalchemy import TIMESTAMP, Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from entities.base import Base
import enum


class EatenItem(Base):
    __tablename__ = 'eaten_items'

    eaten_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    item_type = Column(Integer, nullable=False)
    item_id = Column(Integer, nullable=False)
    date_time = Column(TIMESTAMP, nullable=False)
    amount = Column(Float, nullable=False)

    user = relationship("User", back_populates="user_eaten_items")
