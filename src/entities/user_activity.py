from sqlalchemy import Column, Integer, ForeignKey, Float, TIMESTAMP
from sqlalchemy.orm import relationship
from entities.base import Base


class UserActivity(Base):
    __tablename__ = 'user_activities'

    activity_id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    calories_burned = Column(Float, nullable=False)
    date_time = Column(TIMESTAMP, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    activity_type_id = Column(Integer, ForeignKey("activity_types.activity_type_id"))

    user = relationship("User", back_populates="user_activities")
    activity_type = relationship("ActivityType", back_populates="user_activities")
