from sqlalchemy import Column, String, Boolean, DateTime
from .base import UUIDModel, TimestampModel

class ParticipantBase(object):
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    gender = Column(String)
    dob = Column(DateTime)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    address_line_city = Column(String)
    address_postcode = Column(String)
    address_country = Column(String)
    phone_num = Column(String)
    emergency_con_name = Column(String)
    emergency_con_num = Column(String)

class Participants(ParticipantBase, UUIDModel, TimestampModel):
    __tablename__ = "participants"

