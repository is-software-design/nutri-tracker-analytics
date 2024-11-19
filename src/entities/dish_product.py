from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from entities.base import Base


class DishProduct(Base):
    __tablename__ = 'DishProduct'

    dish_product_id = Column(Integer, primary_key=True)
    dish_id = Column(Integer, ForeignKey("Dish.dish_id"))
    product_id = Column(Integer, ForeignKey("Product.product_id"))
    mass = Column(Float, nullable=False)

    dishes = relationship("Dish", back_populates="products")
    products = relationship("Product", back_populates="dishes")