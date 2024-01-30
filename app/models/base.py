from sqlalchemy import Column, UUID, DateTime, String
import uuid
from datetime import datetime

class UUIDModel(object):
    id = Column(
        String, 
        primary_key=True,
        default=lambda: str(uuid.uuid4()), 
        index=True)

class TimestampModel(object):
    last_updated_at = Column(
        DateTime,
        default=datetime.utcnow, 
        onupdate=datetime.utcnow,
        nullable=False
    )
    created_at = Column(
        DateTime,
        default=datetime.utcnow, 
        onupdate=datetime.utcnow,
        nullable=False
    )