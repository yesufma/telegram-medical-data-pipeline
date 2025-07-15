from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DimChannel(Base):
    __tablename__ = "dim_channels"
    channel_id = Column(Integer, primary_key=True)
    channel_name = Column(String)

class DimDate(Base):
    __tablename__ = "dim_dates"
    date_id = Column(Integer, primary_key=True)
    date = Column(DateTime)

class FctMessage(Base):
    __tablename__ = "fct_messages"
    message_id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey("dim_channels.channel_id"))
    date_id = Column(Integer, ForeignKey("dim_dates.date_id"))
    text = Column(String)
    has_image = Column(Boolean)
    channel = relationship("DimChannel")
    date = relationship("DimDate")

class FctImageDetection(Base):
    __tablename__ = "fct_image_detections"
    detection_id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey("fct_messages.message_id"))
    detected_object = Column(String)
    message = relationship("FctMessage")
