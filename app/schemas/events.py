from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import List
from uuid import UUID
from .participants import participantsSchema

class eventsSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    event_id: str
    race_id: str
    ticket_id: str
    event_title: str
    race_title: str
    ticket_title: str
    created_at: str
    updated_at: str

class eventStartListSchema(eventsSchema):
    participant: participantsSchema

class eventStartListsSchema(eventsSchema):
    participants: List[participantsSchema]