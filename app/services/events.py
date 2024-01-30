from typing import Any, List
from sqlalchemy.sql.expression import Executable
from .base import BaseService, BaseDataManager
from app.schemas.events import eventStartListSchema, eventsSchema
from app.schemas.participants import participantsSchema
from app.models.participants import Participants
import json
from app.db_connection import filename

class EventsService(BaseService):
    async def get_all_startlists(self) -> List[eventStartListSchema]:
        return await EventsDataManager(self.db).get_all_startlists()
    async def create_startlist(self, data) -> eventStartListSchema:
        return await EventsDataManager(self.db).create_startlist(data=json.loads(data))

class EventsDataManager(BaseDataManager):
    async def get_all_startlists(self) -> List[eventStartListSchema]:
        all_start_lists = self.get_all()
        res = []
        for start_list in all_start_lists:
            res.append(self.process_startlist(start_list))
        return res
    
    async def create_startlist(self, data: dict) -> eventStartListSchema:
        self.db.append(data)
        with open(filename, 'w') as f:
            json.dump(self.db, f)
        return self.process_startlist(item=data)
    
    def process_startlist(self, item: dict) -> eventStartListSchema:
        event_model = eventsSchema(
            id=item["id"],
            event_id=item["eventId"],
            race_id=item["raceId"],
            ticket_id=item["ticketId"],
            event_title=item["eventTitle"],
            race_title=item["raceTitle"],
            ticket_title=item["ticketTitle"],
            created_at=item["createdAt"],
            updated_at=item["updatedAt"]
        )
        participant_info = item["fields"]
        info_dict = {}
        for d in participant_info:
            info_dict[d["name"]] = d["value"]
        participant_model = participantsSchema(
            first_name=info_dict["First Name"],
            last_name=info_dict["Last Name"],
            email=info_dict["Email Address"],
            gender=info_dict["Gender"],
            dob=info_dict["Date of Birth"],
            address_line_1=info_dict["Address (Line 1)"],
            address_line_2=info_dict["Address (Line 2)"],
            address_line_city=info_dict["Address (City)"],
            address_postcode=info_dict["Address (Postcode)"],
            address_country=info_dict["Address (Country)"],
            phone_num=info_dict["Phone Number"],
            emergency_con_name=info_dict["Emergency Contact"],
            emergency_con_num=info_dict["Emergency Phone"]
        )
        event_start_list_data = event_model.model_dump()
        event_start_list_data["participant"] = participant_model
        return eventStartListSchema(**event_start_list_data)

