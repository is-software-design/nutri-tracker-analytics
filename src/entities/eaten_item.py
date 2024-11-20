from sqlalchemy import TIMESTAMP, Column, Integer, ForeignKey, Enum as SaEnum, Float
from sqlalchemy.orm import relationship
from entities.base import Base
import enum


class ItemType(enum.Enum):
    dish = "dish"
    product = "product"


class EatenItem(Base):
    __tablename__ = 'EatenItem'

    eaten_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.user_id"))
    item_type = Column(SaEnum(ItemType), nullable=False)
    item_id = Column(Integer, nullable=False)
    date_time = Column(TIMESTAMP, nullable=False)
    amount = Column(Float, nullable=False)

    user = relationship("User", back_populates="user_eaten_items")
