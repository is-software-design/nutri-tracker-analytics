from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from entities.base import Base


class ActivityType(Base):
    __tablename__ = 'activity_types'

    activity_type_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    calories_burned_per_unit = Column(Float, nullable=False)

    user_activities = relationship("UserActivity", back_populates="activity_type")
