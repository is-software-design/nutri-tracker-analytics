from sqlalchemy import TIMESTAMP, Column, Integer, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship
from src.entities.base import Base


class EatenItem(Base):
    __tablename__ = 'EatenItem'

    eaten_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.user_id"))
    item_type = Column(Enum("dish", "product", name="item_type"), nullable=False)
    item_id = Column(Integer, nullable=False)
    date_time = Column(TIMESTAMP, nullable=False)
    amount = Column(Float, nullable=False)

    user = relationship("User", back_populates="user_eaten_items")
