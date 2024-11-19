from sqlalchemy import Column, Integer, String, Date, Enum, Float
from sqlalchemy.orm import relationship
from entities.base import Base


class User(Base):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    activity_level = Column(Enum("high", "low", "medium", name="activity_level"),
                            nullable=False)
    goal = Column(Enum("diet", "weight gain", name="goal"), nullable=False)

    user_activities = relationship("UserActivity", back_populates="user")
    user_products = relationship("Product", back_populates="owner")
    user_dishes = relationship("Dish", back_populates="owner")
    user_eaten_items = relationship("EatenItem", back_populates="user")