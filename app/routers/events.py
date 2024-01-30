from fastapi import APIRouter, status, Depends, Form, Request
from typing import List
from app.schemas.events import eventStartListSchema
from sqlalchemy.orm import Session
from app.db_connection import get_db
from app.services.events import EventsService

router = APIRouter()

@router.get(path="/startlists", status_code=status.HTTP_200_OK, response_model=List[eventStartListSchema])
async def get_all_startlists(
    db: list[dict] = Depends(get_db)
) -> List[eventStartListSchema]:
    return await EventsService(db=db).get_all_startlists()

@router.post(path="/startlists", status_code=status.HTTP_201_CREATED, response_model=eventStartListSchema)
async def create_startlist(
        request: Request, 
        db: list[dict] = Depends(get_db)
) -> eventStartListSchema:
    return await EventsService(db=db).create_startlist(data=await request.body())