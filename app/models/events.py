from sqlalchemy import Column, String, Boolean, DateTime
from .base import UUIDModel, TimestampModel

class EventBase(object):
    event_id = Column(String, unique=True)
    race_id = Column(String)
    ticket_id = Column(String)
    event_title = Column(String)
    race_title = Column(String)
    ticket_title = Column(String)

class Events(EventBase, UUIDModel, TimestampModel):
    __tablename__ = "events"
