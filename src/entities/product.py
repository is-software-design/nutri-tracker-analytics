from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from entities.base import Base


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    average_mass = Column(Float, nullable=False)
    calories_per_100g = Column(Float, nullable=False)
    proteins_per_100g = Column(Float, nullable=False)
    fats_per_100g = Column(Float, nullable=False)
    carbs_per_100g = Column(Float, nullable=False)
    ispublic = Column(Boolean, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)

    owner = relationship("User", back_populates="user_products")
    dishes = relationship("DishProduct", back_populates="products")
