from pydantic import BaseModel, EmailStr, ConfigDict
from uuid import UUID

class participantsSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    first_name: str
    last_name: str
    email: str
    gender: str
    dob: str
    address_line_1: str
    address_line_2: str
    address_line_city: str
    address_postcode: str
    address_country: str
    phone_num: str
    emergency_con_name: str
    emergency_con_num: str